from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('information/', views.information),
    path('news/', views.news),
    path('contact/', views.contact)
]