from django.shortcuts import render
import json
from django.http.response import HttpResponse

# dict data, xml보다 비교하여 light weight data라고 불린다.
# lan={
#     'id':123,
#     'name':'파이썬',
#     'history':[
#         {'date':'2023-10-25','exam':'basic'},
#         {'date':'2023-10-26','exam':'django'},
#     ]
# } #python 에서는 dict로 받는다  json encoding-decoding 을 알아야 한다.

def testFunc():
    # print(type(lan)) #<class 'dict'> dict 타입
    # #python object(dict,list,tuple 등)을 문자열로 변환-Json encoding
    # #Json 모양의 문자열을 python object(dict)로 변환할 수 있다.-Json decoding
    # jsonString =json.dumps(lan) #json encoding하고 있음 : dict->str
    # print(jsonString) #<class 'dict'>
    # print(type(jsonString)) # <class 'str'> string으로 타입이 바뀜 - js가 객체로 이해할 수 있음
    # jsonString =json.dumps(lan,indent=4) #json encoding하고 있음+들여쓰기해줌
    # print(jsonString)
    # # print(jsonString['name']) #문자열로 변환되어있기에 키처럼 생겼지만 문자열이므로 dict타입의 문법이 안먹는다.
    #
    # print('*'*30)
    # dictData =json.loads(jsonString) #json decoding str->dict
    # print(dictData)
    # print(type(dictData)) #<class 'dict'>
    # print(dictData['name']) #키를 썼기에 dict이므로 value값이 나온다.
    # for h in dictData['history']:
    #     print(h['date'],h['exam'])
    pass
    

# Create your views here.
def MainFunc(request):

    
    return render(request,'abc.html')

def Func1(request):
    msg=request.GET.get('msg')
    msg="nice "+msg #문자열
    print(msg)
    context={'key':msg} #dict
    return HttpResponse(json.dumps(context),content_type="application/json") #파이썬의 dict나 list string을 json형식으로 바꿔주고 싶을 때는 dumps로 넘겨주면 된다. dict->string, json 모양은 유지되고 시스템에게 알려주기
# 웹상에서 데이터를 넘길때는 문자열만 넘길수 있다. 문자열로 잘게 잘게 잘라 패킷단위로 이진데이터 형식으로 넘기는 것

def Func2(request):
    mydata=[
        {'irum':'tom1','nai':22},
        {'irum':'tom2','nai':23},
        {'irum':'tom3','nai':24}
    ] #자바스크립에서는 이게 배열의 요소가 되는것, 파이썬의 dict와 java의 json 형태와 닮아있다.
    return HttpResponse(json.dumps(mydata),content_type="application/json")

