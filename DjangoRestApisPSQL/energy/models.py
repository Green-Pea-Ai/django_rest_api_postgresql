from django.db import models

# Create your models here.
class Wdmodel(models.Model):
	title = models.CharField(max_length=100, blank=False, default='')
	description = models.CharField(max_length=200, blank=False, default='')
	published = models.BooleanField(default=False)