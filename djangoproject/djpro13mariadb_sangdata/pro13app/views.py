from django.shortcuts import render, redirect
import MySQLdb
from pro13app.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')


def ListFunc(request):
    '''
    직접 sql문을 사용하는 방법
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()  # SQL문 실행 및 select의 결과를 기억하는 클래스
        sql="select *from sangdata"
        cursor.execute(sql)
        datas=cursor.fetchall()
        print(datas) #((1, '장갑', 3, 10000), (2, '고무장갑', 2, 12000), (3, '가죽장갑', 10, 50000), (4, '가죽점퍼', 5, 650000), (5, '볼펜', 12, 3350), (6, '볼펜이있나', 12, 6000), (7, '지우개가있나', 10, 1200), (8, '노트가있나', 8, 6500))
        print(type(datas)) #<class 'tuple'>
        
        return render(request,'list.html',{'datas':datas})
    except Exception as err:
        print('에러 : ', err)
        conn.rollback()
        
    finally:
        cursor.close()
        conn.close()

    # return render(request,'list.html')   원래 기존의 우리가 알고 있던 방법 pack1의 test41 참고
    '''
    
    '''
    #페이징을 안한 경우
    datas = Sangdata.objects.all()
    print(datas)  # <QuerySet [<Sangdata: Sangdata object (1)>, <Sangdata: Sangdata object (2)>, <Sangdata: Sangdata object (3)>, <Sangdata: Sangdata object (4)>, <Sangdata: Sangdata object (5)>, <Sangdata: Sangdata object (6)>, <Sangdata: Sangdata object (7)>, <Sangdata: Sangdata object (8)>]>
    print(type(datas))  # <class 'QuerySet'>
    return render(request, 'list.html', {'datas':datas}) 
    '''
    
    #페이징 처리를 한 경우
    datas=Sangdata.objects.all().order_by('-code') #최근 것이 가장 처음에 나오게 하려고 함
    paginator =Paginator(datas,5) #페이지 당 5행씩 출력
    # print(paginator)
    try:
        page=request.GET.get('page')
    except:
        page=1
    
    try:
        data=paginator.page(page)
    except PageNotAnInteger:
        data=paginator.page(1)
    except EmptyPage:
        data=paginator.page(paginator.num_pages())
    
    #개별 페이지 표시 작업용
    allpage=range(paginator.num_pages+1)
    print('allpage:', allpage) #range(0, 4)
    return render(request, 'list2.html',{'datas':data,'allpage':allpage}) #페이징 처리를 한것과 페이징처리를 안한걸 합치면 오류가 나기 때문에 페이징 처리를 한 list2를 새로 만든다., 개별페이지를 보여줄땐 전달하면 allpage로 전달-옵션일뿐, 필수 아님, data는 paginator를 먹었기에 그 기능을 가지고 있다.
    
    
    
def InsertFunc(request):  # insert.html로 가게 해주는것
    return render(request, 'insert.html') 


def InsertOkFunc(request): #db에 저장
    if request.method == 'POST':
        code = request.POST.get("code")
        # 새 상품 code 유무 여부 검증후 insert문 진행
        try:
           Sangdata.objects.get(code=code)
           return render(request, 'insert.html', {'msg':'이미 등록된 번호입니다'}) 
        except Exception as e:
            #추가 작업 
            Sangdata(
                code=code,
                sang=request.POST.get("sang"),
                su=request.POST.get("su"),
                dan=request.POST.get("dan"),
            ).save()
            
            return HttpResponseRedirect("/sangpum/list")
        

def UpdateFunc(request):
    updata =Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html',{'data':updata}) 


def UpdateOkFunc(request): #수정할 자료를 읽어오게 됨- POST 방식
    if request.method=='POST':
        upRecode=Sangdata.objects.get(code=request.POST.get("code"))
        upRecode.code=request.POST.get("code") #변수가 db있던 자료에 있는 값을 우리가 입력한 값으로 덮어쓰게 함
        upRecode.sang=request.POST.get("sang")
        upRecode.su=request.POST.get("su")
        upRecode.dan=request.POST.get("dan")
        upRecode.save()
        
    return redirect('/sangpum/list')
    


def DeleteFunc(request):
    delRecode=Sangdata.objects.get(code=request.GET.get("code"))
    delRecode.delete()
    return redirect('/sangpum/list')



    
    
