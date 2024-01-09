#각각의 application마다 urls을 둬서 원래 urls.py로부터 위임을 받는 것
from django.urls import path
from pro3app import views #같은 경로에 있더라도 꼭 써주어야 한다.

urlpatterns = [
     path('insert',views.InsertFunc), 
     
]

