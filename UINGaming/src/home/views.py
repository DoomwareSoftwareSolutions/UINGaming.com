#!/usr/bin/env python
from django.http import HttpResponse, Http404,  HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from src.utils.api import render_to_json
from src.utils import api
from src.home.models import Slide, Feature, New

def SlidesAPI(request):
	if request.method == 'GET':
		slideList = []
		slidesQuerySet = Slide.getSlides(3)
		for slide in slidesQuerySet:
			slideList.append(slide.getDictionary())
		
		return render_to_json(slideList)
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
   
def objectShouldBeSaved(deserialized_object,returnData):
	# Si los parametros son invalidos
	if deserialized_object is None:
		returnData['error_code'] = 4 # ERROR PARAMETROS INVALIDOS
		returnData['error_description'] = _("Invalid parameters")
		return False;

	return True
    
def FeaturesAPI(request):
	if request.method == 'GET':
		featuresList = []
		featuresQuerySet = Feature.getFeatures(3)
		for feature in featuresQuerySet:
			featuresList.append(feature.getDictionary())
		
		return render_to_json(featuresList)
	#elif request.method == 'POST':

def NewsViewerAPI(request):
	if request.method == 'GET':
		information = {}
		newpk = request.GET.get('pk',None)
		if newpk is None:
			api.set_error(information,1,_("No new was specify"))
			return api.render_to_json(information)
		try:
			new = New.objects.filter(pk=newpk).get()
		except:
			api.set_error(information,2,_("The new does not exist"))
			return api.render_to_json(information)
		
		information = new.toDic()
		api.set_error(information,0,'')
		return api.render_to_json(information)	
	else:
		return HttpResponseNotAllowed(['GET'])
	
def NewsListAPI(request):
	if request.method == 'GET':
		begin = request.GET.get('begin',0)
		end = request.GET.get('end',10)
		information = {}
		news = New.getList(begin,end)
		return api.render_to_json(map(New.toDic,news))
	else:
		return HttpResponseNotAllowed(['GET'])