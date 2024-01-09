from django.shortcuts import render
from pro19app.models import Product
from django.http.response import HttpResponse
import json

# Create your views here.
def MainFunc(request):
    imsi = "<div><h2>메인화면</h2></div>"   # html 형식에 문서를 전송
    return render(request, 'main.html', {'maintag':imsi})

def listFunc(request):
    pdatas = Product.objects.filter(category=1)
    datas = []
    for p in pdatas:
        dic = {'pname':p.pname, 'description':p.description, 'price':p.price}
        datas.append(dic)
    return HttpResponse(json.dumps(datas), content_type='application/json')

def list2Func(request):
    ddatas = Product.objects.filter(category=2)
    datas = []
    for p in ddatas:
        dic = {'pname':p.pname, 'description':p.description, 'price':p.price}
        datas.append(dic)
    return HttpResponse(json.dumps(datas), content_type='application/json')

