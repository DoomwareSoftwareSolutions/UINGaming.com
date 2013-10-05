from django.http import HttpResponse, Http404,  HttpResponseNotAllowed
from django.http import HttpResponse, Http404,  HttpResponseNotAllowed
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core import serializers
from django.core.serializers.json import DeserializationError
from src.utils.api import render_to_json
from django.utils.translation import ugettext as _
import json

from src.users.models import User
from src.utils import Crypt, api

###############################################################################################################################
#####                                                       APIS                                                          #####
###############################################################################################################################

# ########################################################################################### #
# #############################     SESSION INFO API     #################################### #
# ########################################################################################### #

def SessionInfoApi(request):
    if request.method == 'GET':
        information = {}
        username = request.get_signed_cookie('user_id',None)
        if username != None:
            user = User.getByUsername(username)
            information['permission'] = user.permission
            information['pk'] = user.pk
            information['username'] = username
            information['loggedIn'] = True
            return api.render_to_json(information);
        else:
            information['loggedIn'] = False
            return api.render_to_json(information);
        
    else: 
        return HttpResponseNotAllowed(['GET'])  
        

# ########################################################################################### #
# ##################################     SIGNIN API     ##################################### #
# ########################################################################################### #

# Esta view maneja '/signin'. Renderea el formulario de inicio de sesion y valida los datos ingresados
# buscando el usuario en la database.
def SignInAPI(request):
    if request.method == 'POST':
        # POST METHOD: Aca valido la informacion de inicio de sesion
        params = api.json_to_dict(request.body)
        information = {}
    
        # Si los parametros son invalidos
        if params is None:
            api.set_error(information,6,_("Invalid parameters"))
            return api.render_to_json(information);
        
        information['username'] = params.get('username', '')
        password = params.get('password', '')
        remember = params.get('remember',False)
        
        valid = User.isValidLogin(information['username'], password)
        if not valid:
            # ERROR NOMBRE DE USUARIO INEXISTENTE O CONTRASENA INCORRECTA
            api.set_error(information,1,_("Username does not exist or password is incorrect"))
            return api.render_to_json(information)
        else:
            # NO HUBO ERRORES!
            user = User.getByUsername(information['username'])
            api.set_error(information,0)
            response = api.render_to_json(information)
            if not remember:
                Crypt.set_secure_cookie(response,'user_id',information['username'],expires=True) # Expira al cerrar el navegador
                if user.permission == 'AD':
                    Crypt.set_secure_cookie(response,'user_admin',information['username']+'AD',expires=True) # Expira al cerrar el navegador
            else:
                Crypt.set_secure_cookie(response,'user_id',information['username'],expires=False) # No expira la cookie
                if user.permission == 'AD':
                    Crypt.set_secure_cookie(response,'user_admin',information['username']+'admin',expires=False) # Expira al cerrar el navegador
            return response
    else:
        return HttpResponseNotAllowed(['POST'])
                
                
# ########################################################################################### #
# ##################################     SIGNUP API     ##################################### #
# ########################################################################################### #            
                
# Esta view maneja '/signup'. Renderea el formulario de registro y valida los datos ingresados y guarda el nuevo
# usuario en la DB
def SignUpAPI(request):
    if request.method == 'POST':
        # POST METHOD: Aca valido la informacion de creacion de usuario
        # Obtengo los parametros del JSON enviado
        params = api.json_to_dict(request.body)
        information = {}
        
        # Si los parametros son invalidos
        if params is None:
                # ERROR PARAMETROS INVALIDOS
                api.set_error(information,6,_("Invalid parameters"))
                return api.render_to_json(information);
                
        
        # Obtengo la informacon ingresada
        information['username'] = params.get('username', '')
        password = params.get('password', '')
        vpassword = params.get('vpassword', '')
        information['email'] = params.get('email', '')
        information['name'] = params.get('name', '')
        information['lastname'] = params.get('lastname', '')
        information['country'] = params.get('country', '')
        # NO ERROR!
        api.set_error(information,0)
        leave_open = params.get('remember',None)
        
        # Valido los datos.
        if not User.isValidUsername(information['username']):
            # ERROR NOMBRE DE USUARIO INVALIDO
            api.set_error(information,1,_("Invalid username"))
        elif not User.isValidPassword(password):
            # Marco el error de password invaludo
            # ERROR CLAVE INVALIDA
            api.set_error(information,2,_("Invalid password"))
        elif password != vpassword:
            # Marco el error de passwords distintas
            # ERROR CLAVES NO SON IDENTICAS
            api.set_error(information,3,_("Passwords don't match"))
        elif not User.isValidEmail(information['email']):
            # Marco el error de password invaludo
            # ERROR EMAIL INVALIDO
            api.set_error(information,4,_('Invalid mail'))
        else:
            user = User.add(information['username'],password,information['email'],information['name'], information['lastname']);
            if  user == None:
                # Marco el error de usuario ya existente
                # ERROR USUARIO YA EXISTE
                api.set_error(information,5,_("Username already exists"))
        
        
        if information['error-code'] != 0:
            # Hubo un error al crear el usuario. Envio el diccionario en formato json
            return api.render_to_json(information);
        else:
            # Se creo un usuario, redirijo pero seteo la cookie para identificar
            response = api.render_to_json(information)
            Crypt.set_secure_cookie(response,'user_id',information['username'],expires=True) # Expira al cerrar el navegador
            return response
    else:
        return HttpResponseNotAllowed(['POST'])



# ########################################################################################### #
# ##################################    LOGOUT VIEW     ##################################### #
# ########################################################################################### # 
  
# Esta view maneja '/logout'. Se encarga de eliminar la cookie de identificacion de usuario.   
def LogOutAPI(request):
    if request.method == 'GET':
        information = {}
        if request.get_signed_cookie('user_id',None) is None:
            api.set_error(information,1,_("There is no user logged in"))
            return api.render_to_json(information)
        else:
            api.set_error(information,0)
            response = api.render_to_json(information)
            response.delete_cookie('user_id')
            return response
    else:
        return HttpResponseNotAllowed(['GET'])
    
    

# ########################################################################################### #
# #############################     PASSWORD RECOVER API    ################################# #
# ########################################################################################### #

# Esta view maneja '/passwd-recover'. Se encarga de pedir el usuario a recuperar y configurar la cookie de seguridad.
# Ademas envia el mail de recuperacion de contrasenia
def PasswordRecoverAPI(request):
    information = {}
    cookie = request.get_signed_cookie(key='lpwd_ok', default=None)
    if request.method == 'GET':
        # GET METHOD: Si la cookie ya esta seteada, informo que ya esta en "tramite" el cambio de clave
        # si no esta seteada, leo los parametros, los valido.
        # En caso de ser parametos validos, seteo la cookie, envio el mail de recuperacion y informo el exito
        if cookie is None:
            information['recover-cookie'] = False
            return api.render_to_json(information)
        else:
            information['username'] = cookie.split('|')[0]
            information['email'] = cookie.split('|')[1]
            information['recover-cookie'] = True
            return api.render_to_json(information)
    
    elif request.method == 'POST':
        # POST METHOD: Si la cookie ya esta seteada, informo que ya esta en "tramite" el cambio de clave
        # si no esta seteada, informo lo contrario.
        if cookie != None:
            api.set_error(information,1,_("We have already send a password recovery email for your username."))
            return api.render_to_json(information)
        else:
            
            params = api.json_to_dict(request.body)
            if params is None:
                # ERROR PARAMETROS INVALIDOS
                api.set_error(information,6,_('Invalid parameters'))
                return api.render_to_json(information);
            
            information['username'] = params.get('username', None)
            
            if not User.isValidUsername(information['username']):
                api.set_error(information,2,_('Invalid username'))
                return api.render_to_json(information)
            
            else:
                user = User.getByUsername(information['username'])
                
                if user is None:
                    api.set_error(information,3,_("You haven't start the password recovery process"))
                    return api.render_to_json(information)
                
                else:
                    information['email'] = user.email;
                    api.set_error(information,0)
                    
                    response = api.render_to_json(information)
                    Crypt.set_secure_cookie(response,'lpwd_ok',information['username']+ '|' + information['email'] , expires=False,  time=7200)
                    api.sendRecoveryEmail(user);
                    return response
                
            return render_to_response('passwd_recover.html',information,RequestContext(request))
    else:
        return HttpResponseNotAllowed(['POST','GET'])


# ########################################################################################### #
# ########################     PASSWORD RECOVER RESET API    ################################ #
# ########################################################################################### #

def PasswordRecoverResetAPI(request):
    if request.method == 'GET':
        information = {}
        cookie = request.get_signed_cookie(key='lpwd_ok', default=None)
        if cookie is None:
            api.set_error(information,1,_("You haven't start the password recovery process"))
            return api.render_to_json(information)
        else:
            api.set_error(information,0)
            response = api.render_to_json(information)
            response.delete_cookie('lpwd_ok')
            return response
    else:
        return HttpResponseNotAllowed(['GET'])
    
# ########################################################################################### #
# ############################    PASSWD RECOVER FORM VIEW      ############################# #
# ########################################################################################### #
  
# Esta view maneja '/passwd-recover/<user>'. Se encarga de verificar la existencia de la cookie 'lpwd_ok' y cambiar la password
# del solicitante.
def PasswordRecoverFormAPI(request, username):
    if request.method == 'POST':
        # POST METHOD: Realizo la validacion de los datos ingresados y cambio la contrasenia
        information = {}
        params = api.json_to_dict(request.body)
        
        # Si los parametros son invalidos
        if params is None:
                api.set_error(information,6,_('Invalid parameters'))
                return api.render_to_json(information);
        
        cookie = request.get_signed_cookie(key='lpwd_ok', default=None)
        if cookie is None:
            api.set_error(information,1,_("You haven't start the password recovery process"))
            return api.render_to_json(information)
        else:
            information['username'] = cookie.split('|')[0]
            password = params.get('password', '')
            vpassword = params.get('vpassword', '')
            api.set_error(information,0)
            if not User.isValidPassword(password):
                # Marco el error de password invaludo
                api.set_error(information,2,_("Invalid password"))
            elif password != vpassword:
                # Marco el error de passwords distintas
                api.set_error(information,3,_("Passwords don't match"))
            else:
                user = User.getByUsername(information['username'])
                if user is None:
                    # Marco el error de usuario inexistente
                    api.set_error(information,4,_("Username does not exist"))
                    
            if information['error-code'] != 0:
                # Hubo errores
                return api.render_to_json(information)
            else:
                # TODO OK!!
                user.updateUserPassword(password)
                response = api.render_to_json(information)
                response.delete_cookie('lpwd_ok')
                return response
                
    else:
        return HttpResponseNotAllowed(['POST'])
    
# ########################################################################################### #
# ###############################     USER PROFILE API    ################################### #
# ########################################################################################### #

def UserProfileAPI(request, username):
    information={}
    cookie_value = request.get_signed_cookie(key='user_id', default=None)
    if request.method == 'GET':
        # GET METHOD: Devuelve la informacion del usuario recibido en el parametro user.
        # Si la cookie de sesion no esta seteada devuelve error
        if cookie_value is None:
            api.set_error(information,1,_("You are not logged in"))
            return api.render_to_json(information)
        else:
            if username is None:
                api.set_error(information,2,_("You haven't specified the username"))
                return api.render_to_json(information)
            
            user = User.getByUsername(username)
            
            if user is None:
                api.set_error(information,3,_("User does not exist"))
                return api.render_to_json(information);
            
            api.set_error(information,0)
            information = dict(information.items() + user.toDic().items())
            return api.render_to_json(information);

    elif request.method == 'POST':
        # POST METHOD: Cambia la informacion del usuario. Si el usuario no es el que inicio sesion esto no podra llevarse a cabo
        params = api.json_to_dict(request.body)
        if params is None:
            # ERROR PARAMETROS INVALIDOS
            api.set_error(information,6,_('Invalid parameters'))
            return api.render_to_json(information);
        
        if cookie_value == None:
            api.set_error(information,1,_("You are not logged in"))
            return api.render_to_json(information)
        else:
            if username != cookie_value:
                api.set_error(information,2,_("You don't have permision to change this data"))
                return api.render_to_json(information);
        
    
            user = User.getByUsername(username)
            if user is None:
                api.set_error(information,3,_("User does not exist"))
                return api.render_to_json(information);
            
            email = params.get('email', None)
            password = params.get('password', None)
            vpassword = params.get('vpassword', None)
            firstname = params.get('firstname', None)
            lastname = params.get('lastname', None)
            
            if email != None:
                if not User.isValidEmail(email):
                    api.set_error(information,4,_('Invalid email'))
                    return api.render_to_json(information);
                else:
                    user.updateUserEmail(email) # Must save after update
            
            if firstname != None:
                user.updateUserFirstname(firstname) # Must save after update
            if lastname != None:
                user.updateUserLastname(lastname) # Must save after update
            
            if password != None:
                if not User.isValidPassword(password):
                    api.set_error(information,5,_('Invalid password'))
                    return api.render_to_json(information);
                elif password != vpassword:
                    # Marco el error de passwords distintas
                    # ERROR CLAVES NO SON IDENTICAS
                    api.set_error(information,7,_("Passwords don't match"))
                    return api.render_to_json(information);             
                else:
                    user.updateUserPassword(password) # Must save after update
            
            user.save()
            api.set_error(information,0)
            return api.render_to_json(information)
    else:
        return HttpResponseNotAllowed(['POST','GET'])

def UserEditProfile(request):
	returnData = {}

	# Obtengo los parametros del JSON enviado
	try:
		deserialized_object = json.loads(request.body)[0]
	except DeserializationError: 
		returnData['error_code'] = 1 
		returnData['error_description'] = _("Error en la deserializacion del usuario")
		return render_to_json(returnData);
	
	#PK=-1 => ADD
	if (deserialized_object[u'username']==-1):
		#We set the objects id's to None to create a new entry. (DJANGO 1.5.X BUG)
		deserialized_object.id = None
		deserialized_object.pk = None
		deserialized_object.save()	
		return render_to_json(returnData);
	else:
		return userEdit(deserialized_object,returnData)

def userEdit(obj,returnData):
	try:
		user = User.objects.get(pk=obj[u'username'])
		user.firstname = obj[u'firstname']
		user.lastname = obj[u'lastname']
		user.email = obj[u'email']
		user.save()
	except User.DoesNotExist:
		returnData['error_code'] = 2 
		returnData['error_description'] = _("User not found")
	
	return render_to_json(returnData)
