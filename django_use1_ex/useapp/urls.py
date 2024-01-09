from django.contrib import admin
from django.urls import path
from useapp import views


urlpatterns = [
    path('list', views.ListFunc),
    path('cal', views.CalFunc),
    path('graph',views.GraphFunc),
    path('table',views.TableFunc),
]