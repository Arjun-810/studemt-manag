# from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import addStudents


# Create your views here.

def addStudent(request):
    if request.method == "POST":
        students_data=json.loads(request.body)
        mail_id=students_data['mail_id']
        if addStudents.objects.filter(mail_id=mail_id).exists():
            return JsonResponse("EMAIL ALREADY REGISTERED",safe=False)
        else:
            addStudents.objects.create(**students_data)
            return JsonResponse("OK",safe=False)


def studentLogin(request):
    if request.method == "POST":
        login_data=json.loads(request.body)
        mail_id = login_data['mail_id']
        password = login_data['password']
        if addStudents.objects.filter(mail_id__contains=mail_id,password__contains=password).filter(mail_id=mail_id,password=password).exists():
            # return JsonResponse("OK",safe=False)
            return_data=addStudents.objects.filter(mail_id=mail_id).values('id')
            return JsonResponse(list(return_data),safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)


def student_message(request):
    if request.method=="POST":
        message_student_data=json.loads(request.body)
        message=message_student_data['message']
        student_id=message_student_data['student_id']
        addStudents.objects.filter(id=student_id).update(message=message)
        return JsonResponse("OK",safe=False)


def all_seudents(request):
    if request.method=="GET":
        return_data=addStudents.objects.filter(status__contains="OK").values('id','Name','phone_no','mail_id','password','Branch','course','Roll_no')
        return JsonResponse(list(return_data),safe=False)


def delet_student(request):
    if request.method=="POST":
        delet_student_data=json.loads(request.body)
        student_id=delet_student_data['student_id']
        addStudents.objects.filter(id=student_id).update(status="Deactivate")
        return JsonResponse("OK",safe=False)

def this_student(request):
    if request.method=="POST":
        this__student_data=json.loads(request.body)
        student_id=this__student_data['student_id']
        return_data=addStudents.objects.filter(id=student_id).values()
        return JsonResponse(list(return_data),safe=False)

def edit_student(request):
    if request.method=="POST":
        edit_student_data=json.loads(request.body)
        student_id=edit_student_data['student_id']
        phone_no=edit_student_data['phone_no']
        Roll_no=edit_student_data['Roll_no']
        course=edit_student_data['course']
        password=edit_student_data['password']
        mail_id=edit_student_data['mail_id']
        Branch=edit_student_data['Branch']
        Name = edit_student_data['Name']
        addStudents.objects.filter(id=student_id).update(Name=Name,phone_no=phone_no,mail_id=mail_id,Roll_no=Roll_no,course=course,Branch=Branch,password=password)
        return JsonResponse("OK",safe=False)