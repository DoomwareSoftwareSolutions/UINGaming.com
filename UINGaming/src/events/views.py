# Create your views here.
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.utils.api import render_to_json, json_to_dict
from src.events.models import Event
from django.utils.translation import ugettext as _
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
		information = []
		all_entries = Event.objects.all()
		for event in all_entries:
			information.append(event.toDict())
			return render_to_json(information)
	#ADD EVENT
	elif request.method == 'POST':
		# POST METHOD: Aca valido la informacion de creacion de usuario
		# Obtengo los parametros del JSON enviado
		params = json_to_dict(request.body)
		print request.body
		information = {}
	
		# Si los parametros son invalidos
		if params is None:
			information['error_code'] = 6 # ERROR PARAMETROS INVALIDOS
			information['error_description'] = _("Invalid parameters")
			return render_to_json(information);
	
	
		# Obtengo la informacon ingresada
		information['head'] = params.get('head', '')
		information['body'] = params.get('body', '')
		information['image'] = params.get('image', '')
		information['date'] = params.get('date', '')
		information['game'] = params.get('game', '')
		information['error_code'] = 0 # NO ERROR!
	
		# Valido los datos.
		if not Event.isValidDate(information['date']):
			information['error_code'] = 1 # ERROR FECHA INVALIDA
			information['error_description'] = _("Invalid date")
		else:
			event = Event.add(information['head'],information['body'],information['image'],information['game'],	information['date'])
			if	event == None:
				# Marco el error de evento ya existente
				information['error_code'] = 2 # ERROR EVENTO YA EXISTE
				information['error_description'] = _("Event already exists")

		return render_to_json(information);
	else:
		raise PermissionDenied 
		
