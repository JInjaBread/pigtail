from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import MyTokenObtainPairSerializer, MyTokenObtainPairView, StudentAPIVIEW, StudentSubjectAPIVIEW
from account import views

urlpatterns =[
    path('api-token/', MyTokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('student/', StudentAPIVIEW.as_view()),
    path('subject/', StudentSubjectAPIVIEW.as_view())
]
