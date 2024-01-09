from django.shortcuts import render, redirect
from pro10app.models import Guest
from datetime import datetime
from django.utils import timezone
from django.http.response import HttpResponseRedirect

# Create your views here.


def MainFunc(request):
    return render(request, 'main.html')


def ListFunc(request):
    # print(Guest.objects.filter(title__contains='연습'))
    # print(Guest.objects.filter(title='연습'))
    # print(Guest.objects.get(id=1)) #한개 읽을땐 get, 여러개 select로 읽을때는 filter
    
    # select *from pro10app_guest
    gdatas = Guest.objects.all()
    # gdatas=Guest.objects.all().order_by('-id') #정렬방법 '-'를 붙이면 desc가 된다.
    # gdatas=Guest.objects.all().order_by('title','-id') #title:asc,id:desc
    # gdatas=Guest.objects.all().order_by('-id')[0:2]
    return render(request, 'list.html', {'gdatas':gdatas})


def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
   if request.method == 'POST':
        # print(request.POST.get('title'))
        # print(request.POST['title'])
        # insert into pro10app guest(... insert문을 직접쓸때는 물리적인 테이블을 써주어야 함, 그러나 활용 dbrms에 따라 쿼리문이 달라짐

        Guest(# 이런 방식은 모든 rdbms에서 다 똑같음
            title=request.POST['title'],
            content=request.POST['content'],
            regdate=datetime.now()  # python이 지원
            # regdate=timezone.now() #장고가 지원

        ).save()

        # #수정
        # Guest(# 이런 방식은 모든 rdbms에서 다 똑같음
        #     g=Guest.objects.get(id=수정할번호)
        #     g.title=request.POST.get('title'),
        #     g.content=request.POST.get('content'),
        #     # regdate=timezone.now() #장고가 지원
        # ).save()
        #
        #삭제
        # g=Guest.objects.get(id=삭제할번호)   
        # g.delete()

    # return HttpResponseRedirect("/guest/select")   
    return redirect("/guest/select")  # 추가 후 목록보기


