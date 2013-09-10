#!/usr/bin/env python

import hashlib
import bcrypt
import hmac
import random
import string

from datetime import timedelta, datetime

from UINGaming.settings.debug import SECRET_KEY, CRYPT_ALGORITHM



def hash_str(s):
    return hmac.new(SECRET_KEY,s).hexdigest()
    
def encryptString(s):
    return "%s|%s" % (s, hash_str(s))
    
def chechEncryptedString(h):
    val = h.split('|')[0]
    if h == encryptString(val):
        return val
        

# Genero una tira de caracteres random que servira para reforzar el encriptado de la contrasenia y el nombre de usuario
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))
    
# Encripto la informacion del usuario utilizando la salt especificada o, si no se especifica,
# se genera una de forma random
def encryptUserInfo_SHA256(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(str(name) + str(pw) + salt).hexdigest()
    
    return '%s,%s' % (h, salt)
    
# Verifico los datos ingresados por el usuario
def verifyUserInfo_SHA256(name, pw, hashedID):
    salt = hashedID.split(',')[1]
    if (encryptUserInfo_SHA256(name,pw,salt) == hashedID):
        return True
    else:
        return False    


# Encripto la informacion del usuario utilizando la salt generada por la biblioteca de bcrypt.
def encryptUserInfo_BCRYPT(name, pw):
    return bcrypt.hashpw(name + pw,bcrypt.gensalt())

# Verifico los datos ingresados por el usuario   
def verifyUserInfo_BCRYPT(name, pw, hashedID):
    return bcrypt.checkpw(name + pw, hashedID);

# ############################################################################################### #
# ################################      API DE ENCRIPTADO     ################################### #
# ############################################################################################### #

# Encripto la informacion del usuario utilizando el algoritmo configurado
def encryptUserInfo(name, pw):
    if CRYPT_ALGORITHM == 'SHA256':
        return encryptUserInfo_SHA256(name, pw)
    elif CRYPT_ALGORITHM == 'BCRYPT':
        return encryptUserInfo_BCRYPT(name, pw)
    else:
        return name+pw

# Verifico los datos ingresados por el usuario   
def verifyUserInfo(name, pw, hashedID):
    if CRYPT_ALGORITHM == 'SHA256':
        return verifyUserInfo_SHA256(name, pw, hashedID)
    elif CRYPT_ALGORITHM == 'BCRYPT':
        return verifyUserInfo_BCRYPT(name, pw, hashedID)
    else:
        return name+pw == hashedID
    
    
# ############################################################################################### #
# ###########################      API PARA COOKIES SEGURAS     ################################# #
# ############################################################################################### #
    
def set_secure_cookie(response, key, value, expires=False, time=None):
    if expires:
        response.set_signed_cookie(key, value)
    else:
        if time is None:
            max_age = 365*24*3600 #1 year
        else:
            max_age = time
        expiration_time = datetime.strftime(datetime.utcnow() + timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_signed_cookie(key=key,value=value, max_age=max_age , expires=expiration_time)
    
    return response
    