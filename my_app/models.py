from datetime import datetime
from django.db import models

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField(default=datetime.now)
    body = models.TextField()
    expired = models.CharField(default="Hello", max_length=100)





