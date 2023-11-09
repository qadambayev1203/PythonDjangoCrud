from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
    path('detail/<int:pk>/', DetailClass.as_view(), name='detail'),
    path('create/', CreateClass.as_view(), name='create'),
    path('update/<int:pk>/', UpdateClass.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteClass.as_view(), name='delete'),
]
