from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re

from src.utils import Crypt

username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_re = re.compile(r"^.{3,20}$") 
email_regexp = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=40, unique = True)
	hashedID = models.CharField(max_length=256)
	created = models.DateField(auto_now_add=True)
	email = models.EmailField()
	
	# Aca va mas informacion del usuario que tenemos que agregar ademas en el metodo ADD
	firstname = models.CharField(max_length=40, blank=True)
	lastname = models.CharField(max_length=40, blank=True)
	
	# TODO: AGREGAR CAMPOS QUE FALTEN
	
	def __unicode__(self):
		return self.username + " - " + self.email
		
	# Debemos agregar aqui la informacion adicional que podea el usuario,
	# para poder inicializarlo correctamente
	@classmethod
	def add(self, username, passwd, email, firstname = '', lastname = ''):
		hashedID = Crypt.encryptUserInfo(username,passwd)
		if User.objects.filter(username = username).count() != 0:
			return None
		u = User(username = username,hashedID = hashedID, email = email, firstname = firstname, lastname = lastname)
		u.save()
		return u

	@classmethod
	def getByPartialUsername(self, partialUsername):
		return User.objects.get(username__iregex=r'^{0}'.format(partialUsername))

	@classmethod
	def getByUsername(self, username):
		try:
			user = User.objects.filter(username = username).get()
		except ObjectDoesNotExist:
			return None
		
		return user
	
	@classmethod
	def isValidLogin(self, username, passwd):
		user = User.getByUsername(username)
		if not user:
			return False
		# Si el usuario existe, chequeo su correspondiente hash con el generado con la informacion
		# que se recibio.
		return Crypt.verifyUserInfo(username,passwd,user.hashedID)
		
		
	@classmethod
	def isValidUsername(self, username):
		# Logica de validacion de usuario
		if username_re.match(username) is None:
			return False
		return True
	
	@classmethod
	def isValidPassword(self, password):
		# Logica de validacion de contrasenia
		if password_re.match(password) is None:
			return False
		return True
	
	@classmethod
	def isValidEmail(self, email):
		# Logica de validacion de email
		if email_regexp.match(email) is None:
			return False
		return True
	
	def updateUserPassword(self, passwd):
		newHash = Crypt.encryptUserInfo(self.username,passwd)
		User.objects.filter(username = self.username).update(hashedID = newHash)
	
	def updateUserEmail(self, newEMail):
		User.objects.filter(username = self.username).update(email = newEMail)
	
	def updateUserFirstname(self, newFirstname):
		User.objects.filter(username = self.username).update(firstname = newFirstname)
		
	def updateUserLastname(self, newLastname):
		User.objects.filter(username = self.username).update(lastname = newLastname)
