from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image, ImageForm


# Create your views here.
def index(request):
    images_list = Image.objects.all()
    context = {'images_list': images_list}
    return render(request, 'gallery/index.html', context)


def add_image(request):
    if request.method == 'POST':  # Si se enviaron datos para almacenar
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('images:index'))
    else:  # No se enviaron datos para almacenar, se muestra el formulario
        form = ImageForm()

    return render(request, 'gallery/image_form.html', {'form': form})

