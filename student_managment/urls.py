from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('students/', include('addStudent.urls')),
    path('query/', include('query.urls'))
]
    