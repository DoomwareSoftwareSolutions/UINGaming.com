# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.events.models import Event,EventMembership
from src.users.models import User
from django.utils.translation import ugettext as _
from django.core import serializers
from django.core.exceptions import *
from django.core.serializers.json import DeserializationError
from src.utils.api import render_to_json

def EventsAPI(request):
	#QUERY ALL EVENTS
	if request.method == 'GET':
		eventPk = request.GET.get('pk')
		#Sin params
		if eventPk == None:
			data = serializers.serialize("json", Event.objects.all())
			response = HttpResponse(data, content_type='application/json')
			return response
		else:
			try:
				data = serializers.serialize("json",Event.objects.filter(pk=eventPk))
				response = HttpResponse(data, content_type='application/json')
				return response
			except Event.DoesNotExist:
				returnData = {}
				returnData['error_code'] = 3 # Event Not Found!
				returnData['error_description'] = _("Event not found")
				return render_to_json(returnData);
				
	#ADD EVENT
	elif request.method == 'POST':
		returnData = {}
		returnData['error_code'] = 0 # NO ERROR!
		returnData['error_description'] = ""
		# Obtengo los parametros del JSON enviado
		try:
			for obj in serializers.deserialize("json", request.body):
				deserialized_object = obj.object
		except DeserializationError: #Lo unico que causa error de deserializacion es el formato de la fecha
			returnData['error_code'] = 1 # ERROR FECHA INVALIDA
			returnData['error_description'] = _("Invalid date")
			return render_to_json(returnData);
		
		#PK=-1 => ADD
		if (deserialized_object.pk==-1):
			#We set the objects id's to None to create a new entry. (DJANGO 1.5.X BUG)
			deserialized_object.id = None
			deserialized_object.pk = None
			deserialized_object.save()	
			return render_to_json(returnData);
		else:
			return editEvent(deserialized_object,returnData)
	else:
		return HttpResponseNotAllowed(['GET'],['POST'])
		

def editEvent(obj,returnData):
	try:
		event = Event.objects.get(pk=obj.pk)
		event = obj
		event.save()
	except Event.DoesNotExist:
		returnData['error_code'] = 2 # ERROR event not found
		returnData['error_description'] = _("Invalid event key")
	
	return render_to_json(returnData)
	
#TODO separar los edits y adds en servicios distintos, el que inserta no sabe pk
#OPCION: reservar pk=1 para inserciones (hice esto en events)

#Reminder: estoy queryando users y events por pk (primary key, por defecto un integer incremental)
def EventMembershipAPI(request):
	#Query the corresponding membership to the passed eventID. Returns the membership in json format
	if request.method == 'GET':
		eventPk = request.GET['pk']
		data = serializers.serialize("json", EventMembership.getByEvent(eventPk))
		response = HttpResponse(data, content_type='application/json')
		return response
	elif request.method == 'POST':
		returnData = {}
		returnData['error_code'] = 0 # NO ERROR!
		returnData['error_description'] = ""
		try:
			for obj in serializers.deserialize("json", request.body):
				deserialized_object = obj.object
		except DeserializationError: 
			returnData['error_code'] = 1 
			returnData['error_description'] = _("Invalid JSON")
			return render_to_json(returnData);
		
		if deserialized_object is None:
			returnData['error_code'] = 2 # ERROR objeto vacio
			returnData['error_description'] = _("Invalid parameters")
			return render_to_json(returnData)
			
		#PK=-1 => ADD
		if (deserialized_object.pk==-1):
			#ADD
			deserialized_object.id = None
			deserialized_object.pk = None
			return addMembership(request,deserialized_object,returnData)
		else:
			#EDIT
			return editMembership(deserialized_object,returnData)
	else:
		return HttpResponseNotAllowed(['GET'],['POST'])





def addMembership(request,obj,returnData):
	cookie_value = request.get_signed_cookie(key='user_id', default=None)
	user = User.getByUsername(cookie_value)
	if user is None:
		returnData['error_code'] = 3 # ERROR invalid user
		returnData['error_description'] = _("Invalid user")
		return render_to_json(returnData)

	try:
		event = Event.objects.filter(pk=obj.event.pk)[0]
	except Event.DoesNotExist:
		returnData['error_code'] = 4 # ERROR invalid event
		returnData['error_description'] = _("Invalid event")
		return render_to_json(returnData)
		
	memb = obj
	memb.user=user
	memb.event = event		
	
	memb.save()
	return render_to_json(returnData)
	
#Edits membership paid status, teamName & teamMembers based on received json
def editMembership(obj,returnData):
	try:
		cookie_value = request.get_signed_cookie(key='user_id', default=None)
		membership = EventMembership.objects.get(pk=obj.pk)
		membership = obj
		membership.save()
	except EventMembership.DoesNotExist:
		returnData['error_code'] = 5 # ERROR membership not found
		returnData['error_description'] = _("Invalid membership key")
	
	
	return render_to_json(returnData)
	


