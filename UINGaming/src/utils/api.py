from django.http import HttpResponse
import json

def render_to_json(dictionary):
    json_txt = json.dumps(dictionary)
    response = HttpResponse(json_txt, content_type='application/json')
    return response