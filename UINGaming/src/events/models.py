from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.core import serializers
import re

import datetime


# Create your models here.

class Event(models.Model):
	head = models.CharField(max_length=256)
	body = models.CharField(max_length=256)
	image = models.CharField(max_length=256)
	game = models.CharField(max_length=256)

	date = models.DateTimeField()
	inscriptionDeadline = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)
	
		
	# TODO: AGREGAR CAMPOS QUE FALTEN

		
	# Debemos agregar aqui la informacion adicional del evento
	# para poder inicializarlo correctamente
	@classmethod
	def add(self, head, body, image, game, date,inscriptionDeadline):
		#checkeo unicidad con head a falta de ideas
		if Event.objects.filter(head=head).count() != 0:
			return None
		e = Event(head=head, body=body, image=image, game=game, date=date, inscriptionDeadline=inscriptionDeadline)
		e.save()
		return e

	@classmethod
	def getByHead(self, head):
		try:
			event = Event.objects.filter(head=head).get()
		except ObjectDoesNotExist:
			return None

		return event
	
	@classmethod
	def isValidDate(self, date):
		try:
			datetime.datetime.strptime(date, '%Y-%m-%d')
		except ValueError:
			return False
		return True
		
	def toDict(self):
		return model_to_dict(self)
	
