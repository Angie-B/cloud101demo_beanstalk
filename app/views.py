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
    month = request.GET.get('month', None)
    var = request.GET.get('var', None)

    filename = "./test.geojson"
    infile = 'Mean_' + month + '_' + var + '.geojson'

    # connect to the bucket
    conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(settings.BUCKET_NAME)

    key = bucket.get_key(infile)
    key.get_contents_to_filename(filename)

    geojsondata = open(filename).read()

    return TemplateResponse(
        request,
        'map_api.html',{
            'title':'MAP_API',
            'message':'Generate the spatial plot for average values',
            #'geojson': geojsondata,
            'month': month,
            'var': var
        }
    )
