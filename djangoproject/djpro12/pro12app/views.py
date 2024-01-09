from django.shortcuts import render
from pro12app.models import Maker, Product
from django.db.models.aggregates import Count,Avg,Sum,StdDev,Variance 

# Create your views here.
def Main(request):
    return render(request,'main.html')

def List1(request):
    makers=Maker.objects.all()
    return render(request,'list1.html',{'makers':makers})
    
    
def List2(request):
    products=Product.objects.all()
    pcount=len(products)
    
    #ORM 함수 연습
    print(products)
    print(products.values_list()) #return type: QuerySet
    
    print(Product.objects.all().count()) #건수를 보여줌 5
    print(products.aggregate(Count('pprice'))) #소계 구하기 {'pprice__count': 5}
    print(products.aggregate(Sum('pprice'))) 
    # print(products.aggregate(Sum('pprice'))['pprice_sum']) #key를 써주면 밸류만 얻을수 있다.
    
    print(products.aggregate(Avg('pprice')))
    print(products.aggregate(StdDev('pprice')))
    
    print()
    aa=products.filter(pname='삼바') #삼바인거 구하기
    print(aa)
    for a in aa.values_list():
        print(a)
    
    print()
    aa=products.exclude(pname='삼바') #삼바를 제외한 나머지 구하기
    print(aa)
    for a in aa.values_list():
        print(a)
    
    
    
    return render(request,'list2.html',{'products':products,'pcount':pcount})
    

def List3(request):
    mid=request.GET.get('id')
    products =Product.objects.filter(pmaker_name=mid) #name이라고 써있다고 name으로 써질필요 없고 타입이 fk이므로 fk라고 보아야 한다. databse에 들어가면 다르게 나오나.
    pcount=len(products)
    
    return render(request,'list2.html',{'products':products,'pcount':pcount})

