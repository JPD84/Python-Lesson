from django.shortcuts import render
from inventory.models import *

def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())
