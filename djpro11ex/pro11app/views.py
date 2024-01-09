from django.shortcuts import render
from pro11app.models import Family
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    fdatas = Family.objects.all()
    total = len(fdatas)
    sum_age = sum(int(f.age) for f in fdatas)
    avg_age = sum_age / total if total > 0 else 0
    return render(request, 'list.html', {'fdatas':fdatas, 'total':total, 'avg_age':avg_age})

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        Family(
            name = request.POST.get('name'),
            age = request.POST.get('age'),
            tel = request.POST.get('tel'),
            gen = request.POST.get('gen'),
        ).save()
    return HttpResponseRedirect("/family/select")