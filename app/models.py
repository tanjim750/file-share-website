from django.db import models
from django.contrib.auth.models import User

class folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

class file(models.Model):
    _folder = models.ForeignKey(folder, on_delete=models.CASCADE)
    files = models.FileField(upload_to='media')
    fileNmae = models.CharField(max_length=50)
    uploaded = models.DateTimeField(auto_now_add=True)