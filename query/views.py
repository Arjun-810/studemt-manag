from django.shortcuts import render
from .models import Query
from django.http import JsonResponse
import json


def AddQuery(request):
    if request.method=="POST":
        data=json.loads(request.body)
        query=data['query']
        id=data['student_id']
        savedata=Query(query=query,student_id=id)
        savedata.save()
        return JsonResponse("success",safe=False)


def StudentViewQuery(request):
    if request.method=="POST":
        student_view_data=json.loads(request.body)
        id=student_view_data['student_id']
        if Query.objects.filter(student_id=id).exists():
            queries = Query.objects.filter(student_id=id).values()
            return JsonResponse( list(queries),safe=False)
        else:
            return JsonResponse("student not exist",safe=False)


def TeacherViewQuery(request):
    if request.method=="GET": 
        return_data=Query.objects.filter(status__contains="PENDING").values('id','student_id','query','date')
        return JsonResponse(list(return_data),safe=False)
   

def AnswerQuery(request):
    if request.method=="POST":
        data=json.loads(request.body)
        answer=data['answer']
        id=data['student_id']
        if Query.objects.filter(student_id=id).exists():
            Query.objects.filter(student_id=id).update(answer=answer,status="DONE")
            return JsonResponse("success",safe=False)
        else:
            return JsonResponse("student not exist",safe=False)