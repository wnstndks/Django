from django.urls import path
from pro21app import views


urlpatterns = [
    path('',views.MainFunc),
    path('list',views.ListFunc)
    
]
