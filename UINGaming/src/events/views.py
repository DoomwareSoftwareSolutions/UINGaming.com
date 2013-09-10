# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.utils.api import render_to_json

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
