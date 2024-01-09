from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("초기 요청 처리")

def helloFunc(request):
    msg="django 만세"
    ss="<html><body>django 프로젝트 구현 %s</body></html>"%msg
    return HttpResponse(ss)

def worldFunc(request):
    msg="django 처리 구조 이해"
    return render(request,'show.html',{'msg':msg}) #forwarding이 기본이다.
    
    
#요청에 대한 실질적 처리를 하는 곳