from django.db import models

class teacherDetails(models.Model):
    mailId = models.CharField(max_length=50)
    password = models.CharField(max_length=50)