from django.shortcuts import render
from pro9app.models import Friend

def Main(request):
    return render(request,'main.html')

def DbShow(request):
    datas = Friend.objects.all() 
    count = datas.count()  # 이 부분이 수정되었습니다.
    return render(request,'list.html',{'datas':datas, 'count':count})  
