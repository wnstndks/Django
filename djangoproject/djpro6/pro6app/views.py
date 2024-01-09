from django.shortcuts import render,redirect #render와 redirect는 틀리다 redirect는 요청이므로 redirect에는 값을 담을 수 없다.
from django.http.response import HttpResponseRedirect
from imagecodecs.imagecodecs import NONE

# Create your views here.
def mainFunc(request):
    return render(request, "main.html") #forward

def selectOsFunc(request):
    # print('request.GET : ',request.GET) request.GET :  <QueryDict: {}>
    if "favorite_os" in request.GET: #데이터를 get방식으로 불러오고 
        print(request.GET["favorite_os"]) # 여기서 받은 값으로
        request.session["f_os"]=request.GET["favorite_os"] #여기에 session키를 주는 것, 세션에다가 값을 담아= 세션을 생성  
    
        # return HttpResponseRedirect("showos") #redirect방식: client로부터 showos 요청이 들어오면 redirect방식이니 urls에서 path로 지정된 showOsFunc로 간다.
        return redirect("/showos") #위와 동일한 값을 불러옴
    else:
        return render(request, "selectos.html")
    

def showOsFunc(request): #selectosfunc에서 if를 만나면 여기로 간다.
    # print("showOsFunc 도착")
    dict_context={}
    
    if "f_os" in request.session:
        print('유효시간 : ',request.session.get_expiry_age())
        dict_context['sel_os']=request.session["f_os"]
        dict_context['message']="그대가 선택한 운영체제는 %s"%request.session["f_os"]
    else:
        dict_context['sel_os']=NONE
        dict_context['message']="운영체제를 선택하지 않았군요"
        
    # del request.session["f_os"] #특정 키를 가진 세션 삭제
    request.session.set_expiry(5)
    
    return render(request,'show.html',dict_context)