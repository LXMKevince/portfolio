from django.shortcuts import render
from gallery.models import GALLERY
# Create your views here.


def home(request):
    gallerys = GALLERY.objects
    return render(request, 'home.html', {'gallerys': gallerys})
