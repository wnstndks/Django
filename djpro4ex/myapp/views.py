from django.shortcuts import render
from django.views.generic.base import TemplateView
import random


# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')  # html을 부르기 위해 render(request 사용)


def SelectFunc(request):
        a = random.randint(1, 11)  # java : request.getParameter("name")에 해당
        if(a % 2 == 0):
            gen = "man"
            images = "/images/man.png"
            return render(request, 'show.html', {'gen':gen,'images':images})
        else:
            gen = "girl"
            images = "/images/girl.png"
            return render(request, 'show.html', {'gen':gen, 'images':images})
