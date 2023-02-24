from django.db import models
from django.contrib.auth.models import User
import datetime

class memory(models.Model):
    content=models.TextField(max_length=1000)
    date=models.DateField(('date'),default=datetime.date.today)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

# Create your models here.
