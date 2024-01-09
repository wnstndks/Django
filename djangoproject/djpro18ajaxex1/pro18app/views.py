from django.shortcuts import render
from pro18app.models import Jikwon
from django.http.response import HttpResponse
import json

# Create your views here.
def Main(request):
    return render(request,'show.html')

def List(request):
    name=request.GET['name']
    print(name)
    jdata=Jikwon.objects.select_related('buser_num').filter(jikwon_jik=name)
    print(jdata)
    
    datas=[]
    # QuerySet타입의 jdata를 dict타입으로 저장해, json 형식의 문자열로 클라이언트에 전송
    for j in jdata:
        dicData={'jikwon_no':j.jikwon_no,'jikwon_name':j.jikwon_name,'buser_name':j.buser_num.buser_name}
        datas.append(dicData)
        
    return HttpResponse(json.dumps(datas),content_type='applicatoin/json');
    
