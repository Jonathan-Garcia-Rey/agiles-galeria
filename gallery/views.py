from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Image, ImageForm


# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    context = {'images_list': images_list}
    return HttpResponse(serializers.serialize("json", images_list))


@csrf_exempt
def add_image(request):
    if request.method == 'POST':
        newImage = Image(
            name=request.POST.get('name'),
            url=request.POST.get('url'),
            description=request.POST.get('description'),
            type=request.POST.get('type'),
            imageFile=request.FILES['imageFile'])
        newImage.save()
    return HttpResponse(serializers.serialize("json", [newImage]))


@csrf_exempt
def viewImages(request):
    return render(request, "gallery/index.html")


def add_new_image(request):
    return render(request, "gallery/image_form.html")
