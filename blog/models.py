from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=100)
    message = models.CharField(max_length=500)

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()