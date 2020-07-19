from django.db import models

class studentDetails(models.Model):
    mailId =  models.CharField(max_length=250)
    password = models.CharField(max_length=500)
 