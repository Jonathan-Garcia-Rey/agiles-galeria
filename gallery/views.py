from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image


# Create your views here.
def index(request):
    images_list = Image.objects.all()
    context = {'images_list': images_list}
    return render(request, 'gallery/Index.html', context)
