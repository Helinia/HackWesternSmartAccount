from django.db import models

from django.contrib.auth.models import User

class Graph(Models.model):
    descrip = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
