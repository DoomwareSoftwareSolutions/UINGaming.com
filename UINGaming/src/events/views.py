# Create your views here.
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.utils.api import render_to_json, json_to_dict
from src.events.models import Event
from django.utils.translation import ugettext as _
from django.core import serializers
from django.core.exceptions import *
"""
def EventsAPI(request):
    event1 = dict(heading='Best Lee Sin',
		body='1v1 top. Lee Sin Only',
		link='',
		image='static/img/event.png'
    )
    event2 = dict(heading='Diamond Only',
		body='5v5 Diamond rank only',
		link='',
		image='static/img/event.png'
    )
    event3 = dict(heading='Bronze Div',
		body='Bronze division tournament! Noob spree!',
		link='',
		image='static/img/event.png'
    ) 
    eventList = [event1, event2, event3]
    return render_to_json(eventList)
"""

def EventsAPI(request):
	#QUERY ALL EVENTS
	if request.method == 'GET':
		information = ""
		data = serializers.serialize("json", Event.objects.all())
		response = HttpResponse(data, content_type='application/json')
		return response
	#ADD EVENT
	elif request.method == 'POST':
		# Obtengo los parametros del JSON enviado
		for obj in serializers.deserialize("json", request.body):
			deserialized_object = obj
		information = {}
		information['error_code'] = 0 # NO ERROR!
		information['error_description'] = ""
		if objectShouldBeSaved(deserialized_object,information):
			#We set the objects id's to None to create a new entry. (DJANGO 1.5.X BUG)
			deserialized_object.object.id = None
			deserialized_object.object.pk = None
			deserialized_object.save()	
	
		return render_to_json(information);
	else:
		raise PermissionDenied 
		
def objectShouldBeSaved(deserialized_object,information):
	# Si los parametros son invalidos
	if deserialized_object is None:
		information['error_code'] = 4 # ERROR PARAMETROS INVALIDOS
		information['error_description'] = _("Invalid parameters")
		return False;
	return True
	
	
		
