"""
Definition of views.
"""
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    """Renders the home page."""
    # assert isinstance(request, HttpRequest)
    return TemplateResponse(request, 'app/index.html', {
            'title':'Home Page'
        })

def map_api(request):
    """Renders the map page."""
    # assert isinstance(request, HttpRequest)
    month = request.GET.get('month', None)
    var = request.GET.get('var', None)

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
