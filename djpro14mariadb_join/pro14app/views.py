from django.shortcuts import render
from pro14app.models import Gogek, Buser, Jikwon

# Create your views here.


def MainFunc(request):
    return render(request, 'main.html')


def ListFunc(request):
    buser = Buser.objects.all()
    return render(request, 'buser.html', {'buser':buser}) 


def FindFunc(request):
    buser = request.GET.get('buser_no')
    jikwons = Jikwon.objects.filter(buser_num=buser)
    
    # 각 jikwon에 대해 연결된 gogeks를 추가합니다.
    for jikwon in jikwons:
        jikwon.gogeks = len(Gogek.objects.filter(gogek_damsano=jikwon.jikwon_no))
    
    return render(request, 'jikwon.html', {'jikwons': jikwons})



def FindGogekFunc(request):
    jikwon = request.GET.get('jikwon_no')
    gogeks = Gogek.objects.filter(gogek_damsano=jikwon).order_by('gogek_name')
    
    for gogek in gogeks:
        jumin = gogek.gogek_jumin
        last_digit = int(jumin[7])
        if last_digit == 1:
            gogek.gender = '남'
        else:
            gogek.gender = '여'
    
    return render(request, 'gogek.html', {'gogeks': gogeks})

