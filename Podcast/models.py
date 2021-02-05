from django.db import models

# Create your models here.
from django.db import models


class Episode(models.Model):
    name = models.CharField(max_length=200)
    published = models.DateTimeField('date published')
    created = models.DateTimeField('date created', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)
    audio = models.FileField()