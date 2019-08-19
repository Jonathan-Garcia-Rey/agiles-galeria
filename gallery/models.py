from django.db import models

# Create your models here.
from django.forms import ModelForm


class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    imageFile = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return "Image: " + self.name


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'url', 'description', 'type', 'imageFile']
