from django.db import models
# from appointment.models import appointments

# Create your models here.


class addStudents(models.Model):
    Name = models.CharField(max_length=50)
    Roll_no = models.CharField(max_length=50)
    mail_id = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=500)
    Branch = models.CharField(max_length=50)
    course = models.CharField(max_length=500)
    message = models.CharField(max_length=500,default="none")
    status=models.CharField(max_length=200,default="OK")
