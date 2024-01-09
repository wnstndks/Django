from django.shortcuts import render

# Create your views here.
#컨트롤러 역할을 한다.
#request가 기본적으로 제공, 클라이너트 요청정보를 가지고 있음
#이 프로젝트는 독립적 누구와도 연결되어있지 않다.

def MainFunc(request):
    return render(request,'index.html')

def Herit1Func(request):
    return render(request,'kbs1.html')


def Herit2Func(request):
    return render(request,'kbs2.html')
