from .models import teacherDetails
from django.http import JsonResponse
import json

def teacherLogin(request):
    if request.method == "POST":
        login_data=json.loads(request.body)
        mailId = login_data['mailId']
        password = login_data['password']
        if teacherDetails.objects.filter(mailId__contains=mailId,password__contains=password).filter(mailId=mailId,password=password).exists():
            return JsonResponse("OK",safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)
