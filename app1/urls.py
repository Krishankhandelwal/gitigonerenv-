from django.urls import URLPattern,path
from app1.views import *

urlpatterns = [
    path('index/',index),
    path('student_list/',Studentcreate),
    path('student_get/<int:pk>/',Studentupdate),
    path('student_apiview/',StudentAPIView.as_view()),
    path('student_apiview/<int:pk>/',StudentAPIView.as_view()),
    path('send-email/', SendEmailView.as_view(), name='send-email'),
    
]
