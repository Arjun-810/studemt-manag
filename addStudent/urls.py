from django.urls import path
from .views import addStudent, all_seudents, delet_student, edit_student, this_student, studentLogin,student_message

urlpatterns = [
    path('login/', studentLogin),
    path('add/', addStudent),
    path('viewStudents/', all_seudents),
    path('delet_student/', delet_student),
    path('edit_student/', edit_student),
    path('this_student/', this_student),
    path('message/', student_message)
]
