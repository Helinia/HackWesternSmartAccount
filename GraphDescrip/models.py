from django.db import models

class GraphDescrip(models.Model):
    description = models.CharField(max_length = 200)
    
