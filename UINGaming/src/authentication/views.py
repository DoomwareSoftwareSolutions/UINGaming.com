from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from UINGaming.settings.debug import *
from src.authentication.models import User
from src.utils import Crypt, api

# ########################################################################################### #
# ##################################    SIGNIN VIEW     ##################################### #
# ########################################################################################### #

# Esta view maneja '/signin'. Renderea el formulario de inicio de sesion y valida los datos ingresados
# buscando el usuario en la database.
def SignInView(request):
        if request.method == 'GET':
            # GET METHOD: Aca envio el formulario de logueo de usuario
            return render_to_response('signin.html',{},RequestContext(request))
        elif request.method == 'POST':
            # POST METHOD: Aca valido la informacion de inicio de sesion
            information = {}
            information['username'] = request.POST.get('username', '')
            password = request.POST.get('password', '')
            leave_open = request.POST.get('remember',None)
            
            valid = User.isValidLogin(information['username'], password)
            if not valid:
                information['error'] = "No existe el nombre de usuario especificado o la clave no es correcta"
                return render_to_response('signin.html',information,RequestContext(request))
            else:
                response = redirect('/')
                if leave_open is None:
                    Crypt.set_secure_cookie(response,'user_id',information['username'],expires=True) # Expira al cerrar el navegador
                else:
                    Crypt.set_secure_cookie(response,'user_id',information['username'],expires=False) # No expira la cookie
                return response
        else:
            raise PermissionDenied  
                
                
# ########################################################################################### #
# ##################################    SIGNUP VIEW     ##################################### #
# ########################################################################################### #            
                
                
# Esta view maneja '/signup'. Renderea el formulario de registro y valida los datos ingresados y guarda el nuevo
# usuario en la DB
def SignUpView(request):
    if request.method == 'GET':
        # GET METHOD: Aca envio el formulario de creacion de usuario
        return render_to_response('signup.html',{},RequestContext(request))
    elif request.method == 'POST':
        # POST METHOD: Aca valido la informacion de creacion de usuario
        information = {}
        valid = True
        
        # Obtengo la informacon ingresada
        information['username'] = request.POST.get('username', '')
        password = request.POST.get('password', '')
        vpassword = request.POST.get('vpassword', '')
        information['email'] = request.POST.get('email', '')
        information['name'] = request.POST.get('name', '')
        information['lastname'] = request.POST.get('lastname', '')
        information['country'] = request.POST.get('country', '')
        leave_open = request.POST.get('remember',None)
        
        # Valido los datos.
        if not User.isValidUsername(information['username']):
            # Marco el error de username invaludo
            valid = False
            information['username_error'] = 'El nombre de usuario no es valido'
        elif not User.isValidPassword(password):
            # Marco el error de password invaludo
            valid = False
            information['password'] = ''
            information['password_error'] = 'La clave no es valida'
        elif password != vpassword:
            # Marco el error de passwords distintas
            valid = False
            information['vpassword'] = ''
            information['password_error'] = 'Las claves no coinciden'
        elif not User.isValidEmail(information['email']):
            # Marco el error de password invaludo
            valid = False
            information['email_error'] = 'El email ingresado no es valido'
        else:
            user = User.add(information['username'],password,information['email'],information['name'], information['lastname']);
            if  user == None:
                # Marco el error de usuario ya existente
                valid = False
                information['username_error'] = 'El usuario ya existe. Ingrese otro'
        
        
        if valid == False:
            # Hubo un error al crear el usuario. Vuelvo a enviar el formulario de creacion con los errores respectivos
            return render_to_response('signup.html',information ,RequestContext(request))
        else:
            # Se creo un usuario, redirijo pero seteo la cookie para identificar
            response = redirect('/')
            response.set_signed_cookie('user_id', information['username'])
            return response
    else:
        raise PermissionDenied
  
  
 
# ########################################################################################### #
# ##################################    LOGOUT VIEW     ##################################### #
# ########################################################################################### # 
  
# Esta view maneja '/logout'. Se encarga de eliminar la cookie de identificacion de usuario.   
def LogOutView(request):
    if request.method == 'GET':
        response = redirect('/')
        response.delete_cookie('user_id')
        return response
    else:
        raise PermissionDenied
  

# ########################################################################################### #
# ###############################    PASSWD RECOVER VIEW     ################################ #
# ########################################################################################### #
  
def sendRecoveryEmail(user):
    url = PASSWORD_RECOVERY_URL + user.username
    message = 'Estimado usuario: \nSi desea recuperar su clave, por favor' + ' ingresar al siguiente link.\n\n' + url + '\n\nMuchas Gracias. UIN Gaming Team'
    send_mail('UIN Gaming - Sistema de recuperacion de clave',message,
              TESTING_ADDRESS, [user.email],fail_silently=False);

# Esta view maneja '/passwd-recover'. Se encarga de pedir el usuario a recuperar y configurar la cookie de seguridad.
# Ademas envia el mail de recuperacion de contrasenia
def PasswordRecoverView(request):
    if request.method == 'GET':
        # GET METHOD: Aca envio el formulario de recuperacion de contrasenia
        cookie = request.get_signed_cookie(key='lpwd_ok', default=None)
        if cookie is None:
            return render_to_response('passwd_recover.html',{},RequestContext(request))
        else:
            information = {}
            information['username'] = cookie.split('|')[0]
            information['email'] = cookie.split('|')[1]
            return render_to_response('passwd_recover_confirm.html',information,RequestContext(request))
    elif request.method == 'POST':
        information = {}
        information['username'] = request.POST.get('username', None)
        if not User.isValidUsername(information['username']):
            information['error'] = 'Por favor ingrese el nombre de usuario correctamente'
        else:
            user = User.getByUsername(information['username'])
            if user is None:
                information['error'] = 'El nombre de usuario especificado no existe'
            else:
                information['email'] = user.email;
                response = redirect('/passwd_recover') #Redirect to confirmation
                Crypt.set_secure_cookie(response,'lpwd_ok',information['username']+ '|' + information['email'] , expires=False,  time=7200)
                sendRecoveryEmail(user);
                return response
            
        return render_to_response('passwd_recover.html',information,RequestContext(request))
    else:
        raise PermissionDenied
 


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
                information['error'] = 'La clave no es valida'
            elif password != vpassword:
                # Marco el error de passwords distintas
                valid = False
                information['error'] = 'Las claves no coinciden'
            
            user = User.getByUsername(information['username'])
            if user is None:
                # Marco el error de usuario inexistente
                valid = False
                information['error'] = 'El usuario no existe'
                
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
        if request.method == 'GET':
            # GET METHOD: Aca envio el formulario de logueo de usuario
            return render_to_response('signin.html',{},RequestContext(request))
        elif request.method == 'POST':
            # POST METHOD: Aca valido la informacion de inicio de sesion
            information = {}
            information['username'] = request.POST.get('username', '')
            password = request.POST.get('password', '')
            leave_open = request.POST.get('remember',None)
            
            valid = User.isValidLogin(information['username'], password)
            if not valid:
                information['error'] = "No existe el nombre de usuario especificado o la clave no es correcta"
                return render_to_response('signin.html',information,RequestContext(request))
            else:
                response = redirect('/')
                if leave_open is None:
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
    if request.method == 'GET':
        # GET METHOD: Aca envio el formulario de creacion de usuario
        return render_to_response('signup.html',{},RequestContext(request)) 
    elif request.method == 'POST':
        # POST METHOD: Aca valido la informacion de creacion de usuario
        information = {}
        
        # Obtengo la informacon ingresada
        information['username'] = request.POST.get('username', '')
        password = request.POST.get('password', '')
        vpassword = request.POST.get('vpassword', '')
        information['email'] = request.POST.get('email', '')
        information['name'] = request.POST.get('name', '')
        information['lastname'] = request.POST.get('lastname', '')
        information['country'] = request.POST.get('country', '')
        information['error_code'] = 0 # NO ERROR!
        leave_open = request.POST.get('remember',None)
        
        # Valido los datos.
        if not User.isValidUsername(information['username']):
            information['error_code'] = 1 # ERROR NOMBRE DE USUARIO INVALIDO
            information['error_description'] = 'El nombre de usuario no es valido'
        elif not User.isValidPassword(password):
            # Marco el error de password invaludo
            information['error_code'] = 2 # ERROR CLAVE INVALIDA
            information['error_description'] = 'La clave no es valida'
        elif password != vpassword:
            # Marco el error de passwords distintas
            information['error_code'] = 3 # ERROR CLAVES NO SON IDENTICAS
            information['error_description'] = 'Las claves no coinciden'
        elif not User.isValidEmail(information['email']):
            # Marco el error de password invaludo
            information['error_code'] = 4 # ERROR EMAIL INVALIDO
            information['error_description'] = 'El email ingresado no es valido'
        else:
            user = User.add(information['username'],password,information['email'],information['name'], information['lastname']);
            if  user == None:
                # Marco el error de usuario ya existente
                information['error_code'] = 5 # ERROR USUARIO YA EXISTE
                information['error_description'] = 'El usuario ya existe. Ingrese otro'
        
        
        if information['error_code'] != 0:
            # Hubo un error al crear el usuario. Envio el diccionario en formato json
            return api.render_to_json(information);
        else:
            # Se creo un usuario, redirijo pero seteo la cookie para identificar
            response = redirect('/')
            response.set_signed_cookie('user_id', information['username'])
            return response
    else:
        raise PermissionDenied

    