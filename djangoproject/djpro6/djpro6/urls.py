"""
URL configuration for djpro6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pro6app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('',views.mainFunc),

    path('setos',views.selectOsFunc), #메인 urls에서 setos라고 이름을 주는 것
    path('showos',views.showOsFunc), #메인 urls에서 setos라고 이름을 주는 것
    #function을 만드는 것 라우팅의 방법은 functionviews를 쓰고 있다.
    
]
