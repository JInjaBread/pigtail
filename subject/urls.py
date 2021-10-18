from django.urls import path
from .views import StudentAPIVIEW, StudentSubjectAPIVIEW
from subject import views

urlpatterns =[
    path('student/', StudentAPIVIEW.as_view()),
    path('subject/', StudentSubjectAPIVIEW.as_view())
]
