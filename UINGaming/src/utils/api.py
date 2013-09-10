from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

import json

from UINGaming.settings.debug import TEMPLATE_DIRS;

def render_to_json(dictionary):
    json_txt = json.dumps(dictionary)
    response = HttpResponse(json_txt, content_type='application/json')
    return response


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
    else:
	raise Http404
	
    return response
    


def PartialsRequestHandler(request, page):
    if request.method == 'GET':
	url = 'partials/' + page + '.html'
        return send_partial(url)
    else:
        pass # TODO POST METHOD

def IndexRequestHandler(request):
    return render_to_response('index.html')
     
