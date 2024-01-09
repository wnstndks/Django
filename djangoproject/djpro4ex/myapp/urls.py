#각각의 application마다 urls을 둬서 원래 urls.py로부터 위임을 받는 것
from django.urls import path
from myapp import views

urlpatterns = [
     path('/select',views.SelectFunc), 
]

