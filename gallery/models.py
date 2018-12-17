from django.db import models

# Create your models here.


class GALLERY(models.Model):

    description = models.CharField(max_length=100)
