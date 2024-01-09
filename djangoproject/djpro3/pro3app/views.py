from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def MainFunc(request):
    return render(request,'index.html') #html을 부르기 위해 render(request 사용)

class CallView(TemplateView):
    template_name='callget.html'
    

def InsertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        irum = request.POST.get("name")     # java : request.getParameter("name")에 해당
        irum = irum + " : 내 친구"
        return render(request, 'list.html', {'irum':irum})


