"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.template import RequestContext
from datetime import datetime
import boto
from django.conf import settings

# Create your views here.
def home(request):
    """Renders the home page."""
    # assert isinstance(request, HttpRequest)
    return TemplateResponse(request, 'app/index.html', {
            'title':'Home Page'
        })

def map_api(request):
    """Renders the about page."""
    # assert isinstance(request, HttpRequest)

    return TemplateResponse(
        request,
        'map_api.html',{
            'title':'MAP_API',
            'message':'Generate the spatial plot for average values'}
    )
