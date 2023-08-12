from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class project(models.Model):
    me = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True, null=True)
    links = models.URLField(max_length=250)
    image_url = models.ImageField(upload_to="images")