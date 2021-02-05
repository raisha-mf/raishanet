from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.models import Episode
def index(request):
    data = "*AAWWeYEAH getchur fruggin Podacst right here bois*"
    eps = Episode.objects.all()
    for ep in eps:
        data += "<br /><br />"
        data += f'<audio controls><source src=“http://127.0.0.1:8000{ep.audio.url}" type="audio/m4a">Unsupported audio file type</audio>'
    return HttpResponse(data)
