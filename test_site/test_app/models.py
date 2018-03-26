from django.db import models

# Create your models here.

class Table1(models.Model):
	field1 = models.CharField(max_length=50)
	field2 = models.CharField(max_length=50)