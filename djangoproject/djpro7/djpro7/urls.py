"""
URL configuration for djpro7 project.

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
from shopapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path('',views.mainFunc), #요청명에 어플리케이션이름 및 프로젝트 이름은 쓰면 안된다.
    path('page1',views.page1Func),
    path('page2',views.page2Func),
    path('cart',views.cartFunc),
    path('buy',views.buyFunc),
    
]
