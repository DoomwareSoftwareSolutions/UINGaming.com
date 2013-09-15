#!/usr/bin/env python
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.utils.api import render_to_json

from src.home.models import Slide, Feature

def SlidesAPI(request):
    slideList = []
    slidesQuerySet = Slide.getSlides(3)
    for slide in slidesQuerySet:
		slideList.append(slide.getDictionary())
    
    return render_to_json(slideList)
    
def FeaturesAPI(request):
    featuresList = []
    featuresQuerySet = Feature.getFeatures(3)
    for feature in featuresQuerySet:
		featuresList.append(feature.getDictionary())
    
    return render_to_json(featuresList)
