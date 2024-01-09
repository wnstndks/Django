from django.shortcuts import render
from pro8app.models import Article

# Create your views here.
def Main(request):
    return render(request,'main.html')

def DbShow(request):
    datas = Article.objects.all() #논리적인 테이블을 쓰고 있음(물리적인 테이블과 연결하기 위하여), 장고의 orm을 사용하고 있는 것
    print(datas) #<QuerySet -> 장고의 결과는 select의 결과를 queryset타입으로 반환하고 있다. 
    print(datas[0].name)
    return render(request,'list.html',{'datas':datas})
