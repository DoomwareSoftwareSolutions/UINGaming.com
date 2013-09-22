# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.events.models import Event,EventMembership
from django.utils.translation import ugettext as _
from django.core import serializers
from django.core.exceptions import *
from django.core.serializers.json import DeserializationError
from src.utils.api import render_to_json

def EventsAPI(request):
	#QUERY ALL EVENTS
	if request.method == 'GET':
		data = serializers.serialize("json", Event.objects.all())
		response = HttpResponse(data, content_type='application/json')
		return response
	#ADD EVENT
	elif request.method == 'POST':
		returnData = {}
		# Obtengo los parametros del JSON enviado
		try:
			for obj in serializers.deserialize("json", request.body):
				deserialized_object = obj
		except DeserializationError: #Lo unico que causa error de deserializacion es el formato de la fecha
			returnData['error_code'] = 2 # ERROR FECHA INVALIDA
			returnData['error_description'] = _("Invalid date")
			return render_to_json(returnData);
			
		
		returnData['error_code'] = 0 # NO ERROR!
		returnData['error_description'] = ""
		if objectShouldBeSaved(deserialized_object,returnData):
			#We set the objects id's to None to create a new entry. (DJANGO 1.5.X BUG)
			deserialized_object.object.id = None
			deserialized_object.object.pk = None
			deserialized_object.save()	
	
		return render_to_json(returnData);
	else:
		return HttpResponseNotAllowed(['GET'],['POST'])
		
def objectShouldBeSaved(deserialized_object,returnData):
	# Si los parametros son invalidos
	if deserialized_object is None:
		returnData['error_code'] = 4 # ERROR PARAMETROS INVALIDOS
		returnData['error_description'] = _("Invalid parameters")
		return False;

	return True
	
def EventMembershipAPI(request):
	#Query the corresponding membership to the passed eventID. Returns the membership in json format
	if request.method == 'GET':
		eventPk = request.GET['pk']
		data = serializers.serialize("json", EventMembership.objects.filter(event__id=eventPk))
		response = HttpResponse(data, content_type='application/json')
		return response
	#ADD/EDIT MEMBERSHIP TODO
	elif request.method == 'POST':
		returnData = {}
		# Obtengo los parametros del JSON enviado
		try:
			for obj in serializers.deserialize("json", request.body):
				deserialized_object = obj
		except DeserializationError: #Lo unico que causa error de deserializacion es el formato de la fecha
			returnData['error_code'] = 2 # ERROR FECHA INVALIDA
			returnData['error_description'] = _("Invalid date")
			return render_to_json(returnData);
			
		
		returnData['error_code'] = 0 # NO ERROR!
		returnData['error_description'] = ""
		if objectShouldBeSaved(deserialized_object,returnData):
			#We set the objects id's to None to create a new entry. (DJANGO 1.5.X BUG)
			deserialized_object.object.id = None
			deserialized_object.object.pk = None
			deserialized_object.save()	
	
		return render_to_json(returnData);
	else:
		return HttpResponseNotAllowed(['GET'],['POST'])

	
	
		
