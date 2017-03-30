"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from djgeojson.views import GeoJSONLayerView
from djgeojson.fields import PolygonField

# Create your views here.
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def map_api(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/map_api.html',
        context_instance = RequestContext(request,
        {
            'title':'MAP_API',
            'message':'Generate the spatial plot for average values',
            'year':datetime.now().year,
        })
    )