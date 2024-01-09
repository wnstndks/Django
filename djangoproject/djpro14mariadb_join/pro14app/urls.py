from django.urls import path
from pro14app import views

urlpatterns = [
        path('list', views.ListFunc),
        path('find', views.FindFunc),
        path('findgogek',views.FindGogekFunc),
]
