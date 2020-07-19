from .views import AddQuery,StudentViewQuery,TeacherViewQuery,AnswerQuery
from django.urls import path


urlpatterns = [
    
    path('addquery/',AddQuery),
    path('student_viewquery/',StudentViewQuery),
    path('teacher_viewquery/',TeacherViewQuery),
    path('teacher_answer_viewquery/',AnswerQuery),
    
]