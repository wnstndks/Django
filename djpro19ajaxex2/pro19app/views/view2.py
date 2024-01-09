from django.shortcuts import render
from pro19app.models import Product
from django.http.response import HttpResponse, HttpResponseRedirect
import json


# Create your views here.
def adminFunc(request):
    return render(request, 'admin.html')


def listFunc(request):
    pdatas = Product.objects.all()
    datas = []
    for p in pdatas:
        dic = {'id':p.id, 'category':p.category, 'pname':p.pname, 'stock':p.stock, 'description':p.description, 'price':p.price}
        datas.append(dic)
    return HttpResponse(json.dumps(datas), content_type='application/json')



def insertFunc(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        pname = request.POST.get('pname')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        description = request.POST.get('description')

        Product.objects.create(
            category=category,
            pname=pname,
            price=price,
            stock=stock,
            description=description
        )

        return render(request, 'admin.html')


