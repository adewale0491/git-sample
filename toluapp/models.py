from django.db import models

# Create your models here.

class studentForm(models.Model):
    fullName = models.CharField(max_length = 100)
    emailAddress = models.CharField(max_length = 100)
    telephone = models.CharField(max_length = 11)
    message = models.CharField(max_length = 100)

