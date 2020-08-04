from django.urls import path
from . import views

urlpatterns = [
    path('', views.gonderi_listesi, name='gonderi_listesi'),
]