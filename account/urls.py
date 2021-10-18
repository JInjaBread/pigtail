from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import MyTokenObtainPairSerializer, MyTokenObtainPairView
from account import views

urlpatterns =[
    path('api-token/', MyTokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]
