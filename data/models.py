from django.db import models



# Create your models here.
class Date(models.Model):
    name = models.CharField(max_length=40)
    value = models.CharField(max_length =60)
    date = models.DateTimeField(auto_now_add=True)