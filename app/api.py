#### Django modules
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseServerError, HttpResponseNotFound
# from django.template import RequestContext
# from django.views.decorators.cache import cache_control
# from django.conf import settings
#
# #### External modules
# from io import BytesIO
# import datetime
import json
# import mimetypes, os
from django.conf import settings
import boto
import boto.s3.connection

def simple_chart(request):

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

    return HttpResponse(json.dumps(geojsondata))
