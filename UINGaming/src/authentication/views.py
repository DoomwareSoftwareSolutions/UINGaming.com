from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.translation import ugettext as _

from src.authentication.models import User
from src.utils import Crypt, api



# ########################################################################################### #
# ############################    PASSWD RECOVER FORM VIEW      ############################# #
# ########################################################################################### #
  
# Esta view maneja '/passwd-recover/<user>'. Se encarga de verificar la existencia de la cookie 'lpwd_ok' y cambiar la password
# del solicitante.
def PasswordRecoverFormView(request, username):
    # GET METHOD: Aca envio el formulario para el cambio de la contrasenia
    if request.method == 'GET':
        cookie = request.get_signed_cookie(key='lpwd_ok', default=None)
        if cookie is None:
            return redirect('/')
        else:
            # Encontro una cookie valida. Renderiza el formulario de cambio de clave
            information = {}
            information['username'] = cookie.split('|')[0]
            information['email'] = cookie.split('|')[1]
            if username != information['username']:
                return redirect('/')
            else:
                return render_to_response('passwd_recover_form.html',information,RequestContext(request))
    elif request.method == 'POST':
        # POST METHOD: Realizo la validacion de los datos ingresados y cambio la contrasenia
        cookie = request.get_signed_cookie(key='lpwd_ok', default=None)
        if cookie is None:
            return redirect('/')
        else:
            information = {}
            information['username'] = cookie.split('|')[0]
            password = request.POST.get('password', '')
            vpassword = request.POST.get('vpassword', '')
            valid = True
            if not User.isValidPassword(password):
                # Marco el error de password invaludo
                valid = False
                information['error'] = _("Invalid Password")
            elif password != vpassword:
                # Marco el error de passwords distintas
                valid = False
                information['error'] = _("Passwords don't match")
            
            user = User.getByUsername(information['username'])
            if user is None:
                # Marco el error de usuario inexistente
                valid = False
                information['error'] = _("Username does not exist")
                
            if not valid:
                # Hubo errores
                return render_to_response('passwd_recover_form.html',information,RequestContext(request))
            else:
                # TODO OK!!
                user.updateUserPassword(password)
                response = redirect('/signin')
                response.delete_cookie('lpwd_ok')
                return response
                
    else:
        raise PermissionDenied
    

###############################################################################################################################
#####                                                       APIS                                                          #####
###############################################################################################################################


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
            information['error_code'] = 6 # ERROR PARAMETROS INVALIDOS
            information['error_description'] = _("Invalid parameters")
            return api.render_to_json(information);
        
        information['username'] = params.get('username', '')
        password = params.get('password', '')
        remember = params.get('remember',False)
        
        valid = User.isValidLogin(information['username'], password)
        if not valid:
            information['error_code'] = 1 # ERROR NOMBRE DE USUARIO INEXISTENTE O CONTRASENA INCORRECTA
            information['error_description'] = _("Username does not exist or password is incorrect")
            return api.render_to_json(information)
        else:
            information['error_code'] = 0 # NO HUBO ERRORES!
            information['error_description'] = ''
            response = api.render_to_json(information)
            if not remember:
                Crypt.set_secure_cookie(response,'user_id',information['username'],expires=True) # Expira al cerrar el navegador
            else:
                Crypt.set_secure_cookie(response,'user_id',information['username'],expires=False) # No expira la cookie
            return response
    else:
        raise PermissionDenied  
                
                
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
                information['error_code'] = 6 # ERROR PARAMETROS INVALIDOS
                information['error_description'] = _("Invalid parameters")
                return api.render_to_json(information);
                
        
        # Obtengo la informacon ingresada
        information['username'] = params.get('username', '')
        password = params.get('password', '')
        vpassword = params.get('vpassword', '')
        information['email'] = params.get('email', '')
        information['name'] = params.get('name', '')
        information['lastname'] = params.get('lastname', '')
        information['country'] = params.get('country', '')
        information['error_code'] = 0 # NO ERROR!
        leave_open = params.get('remember',None)
        
        # Valido los datos.
        if not User.isValidUsername(information['username']):
            information['error_code'] = 1 # ERROR NOMBRE DE USUARIO INVALIDO
            information['error_description'] = _("Invalid username")
        elif not User.isValidPassword(password):
            # Marco el error de password invaludo
            information['error_code'] = 2 # ERROR CLAVE INVALIDA
            information['error_description'] = _("Invalid password")
        elif password != vpassword:
            # Marco el error de passwords distintas
            information['error_code'] = 3 # ERROR CLAVES NO SON IDENTICAS
            information['error_description'] = _("Passwords don't match")
        elif not User.isValidEmail(information['email']):
            # Marco el error de password invaludo
            information['error_code'] = 4 # ERROR EMAIL INVALIDO
            information['error_description'] = _('Invalid mail')
        else:
            user = User.add(information['username'],password,information['email'],information['name'], information['lastname']);
            if  user == None:
                # Marco el error de usuario ya existente
                information['error_code'] = 5 # ERROR USUARIO YA EXISTE
                information['error_description'] = _("Username already exists")
        
        
        if information['error_code'] != 0:
            # Hubo un error al crear el usuario. Envio el diccionario en formato json
            return api.render_to_json(information);
        else:
            # Se creo un usuario, redirijo pero seteo la cookie para identificar
            return api.render_to_json(information);
    else:
        raise PermissionDenied



# ########################################################################################### #
# ##################################    LOGOUT VIEW     ##################################### #
# ########################################################################################### # 
  
# Esta view maneja '/logout'. Se encarga de eliminar la cookie de identificacion de usuario.   
def LogOutAPI(request):
    if request.method == 'GET':
        response = redirect('/')
        response.delete_cookie('user_id')
        return response
    else:
        raise PermissionDenied
    
    

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
            information['error-code'] = 1
            information['error-description'] = _("We have already send a password recovery email for your username.")
            return api.render_to_json(information)
        else:
            
            params = api.json_to_dict(request.body)
            if params is None:
                information['error_code'] = 6 # ERROR PARAMETROS INVALIDOS
                information['error_description'] = _('Invalid parameters')
                return api.render_to_json(information);
            
            information['username'] = params.get('username', None)
            
            if not User.isValidUsername(information['username']):
                information['error-code'] = 2
                information['error-description'] = _('Invalid username')
                return api.render_to_json(information)
            
            else:
                user = User.getByUsername(information['username'])
                
                if user is None:
                    information['error-code'] = 3
                    information['error-description'] = _("You haven\'t start the password recovery process")
                    return api.render_to_json(information)
                
                else:
                    information['email'] = user.email;
                    information['error-code'] = 0
                    information['error-description'] = ''
                    
                    response = api.render_to_json(information)
                    Crypt.set_secure_cookie(response,'lpwd_ok',information['username']+ '|' + information['email'] , expires=False,  time=7200)
                    api.sendRecoveryEmail(user);
                    return response
                
            return render_to_response('passwd_recover.html',information,RequestContext(request))
    else:
        raise PermissionDenied


# ########################################################################################### #
# ########################     PASSWORD RECOVER RESET API    ################################ #
# ########################################################################################### #

def PasswordRecoverResetAPI(request):
    if request.method == 'GET':
        information = {}
        cookie = request.get_signed_cookie(key='lpwd_ok', default=None)
        if cookie is None:
            information['error-code'] = 1
            information['error-description'] = _("You haven\'t start the password recovery process")
            return api.render_to_json(information)
        else:
            information['error-code'] = 0
            information['error-description'] = ''
            response = api.render_to_json(information)
            response.delete_cookie('lpwd_ok')
            return response
    else:
        raise PermissionDenied