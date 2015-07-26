from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import *


def index(request):
    latest_assets = Asset.objects.order_by('-registered')[:5]
    template = loader.get_template('ams/index.html')
    context = RequestContext(request, { 'latest_assets' : latest_assets })
    return HttpResponse(template.render(context))

def asset(request):
    return HttpResponse("stub")

def role(request):
    return HttpResponse("stub")

def details(request,asset_id):
    return HttpResponse("stub")

def create(request):
    return HttpResponse("stub")

def edit(request,asset_id):
    return HttpResponse("stub")
