from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import RequestContext
from django.core.mail import send_mail

import json

from UINGaming.settings.debug import *
from src.authentication.models import User


def set_error(information, error_code, error_description = ''):
	information['error-code'] = error_code 
	information['error-description'] = error_description

def render_to_json(dictionary):
    json_txt = json.dumps(dictionary)
    response = HttpResponse(json_txt, content_type='application/json')
    return response


def json_to_dict(data):
	try:
		data = json.loads(data)
		return data
	except ValueError:
		return None


def send_partial(url):
	response = HttpResponse('', content_type='text/html')
	success = False
	for d in TEMPLATE_DIRS:
		try:
			f = open(d+url,'r')
			success = True
			break
		except IOError:
			try:
				f = open(d+'/'+url,'r')
				success = True
				break
			except IOError:
				try:
					f = open(d+'\\'+url,'r') #Windows compatibility (Si sere capo)
					success = True
					break
				except IOError:
				    continue

	if success:
		content = f.read()
		response.write(content)
		f.close()
	else:
		raise Http404
	
	return response
    

def sendRecoveryEmail(user):
    url = PASSWORD_RECOVERY_URL + user.username
    message = 'Estimado usuario: \nSi desea recuperar su clave, por favor ingresar al siguiente link.\n\n' + url + '\n\nMuchas Gracias. UIN Gaming Team'
    send_mail('UIN Gaming - Sistema de recuperacion de clave',message,
              TESTING_ADDRESS, [user.email],fail_silently=False);


@ensure_csrf_cookie
def PartialsRequestHandler(request, page):
	if request.method == 'GET':
		url = 'partials/' + page + '.html'
		return send_partial(url)
	else:
		pass # TODO POST METHOD


@ensure_csrf_cookie
def IndexRequestHandler(request):
	return render_to_response('index.html', context_instance=RequestContext(request))
    
