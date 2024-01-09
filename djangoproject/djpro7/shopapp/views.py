from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html') #여기서 먼저 적고 main.html를 만들기

def page1Func(request):
     return render(request, 'page1.html')

def page2Func(request):
     return render(request, 'page2.html')

def cartFunc(request):
    name=request.POST["name"] #Post형식으로 받는다.
    price=request.POST["price"]
    # print(name,price)
    product={'name':name, 'price':price}#첫번째 주문상품을
    
    productList=[] #상품이 여러개가 들어올수 있기때문에 List형태로 
    
    if "shop" in request.session: #두번째 주문상품들을 넣는것
        productList=request.session['shop'] #세션을 꺼내와
        productList.append(product) #세션에 그 상품들을 넣어
        request.session['shop']=productList #세션 키에서 뽐아다가 리스트에 넣어? (이 부분 다시 보기)
    else:
        productList.append(product) #첫번째 주문상품 김밥을 만들고 
        request.session['shop']=productList # 김밥통에 넣고 냉장고에 넣는것
        
    print(productList)
    
    context={}
    context['products']=request.session['shop']
    return render(request,'cart.html',context)

def buyFunc(request):
    if "shop" in request.session:
        productList = request.session['shop']
        total=0
        for p in productList:
            total+=int(p['price'])
        print(total)
        
        del request.session['shop'] #특정 세션을 제거
        # request.session.clear() #세션 모두 제거
    
    return render(request,'buy.html',{'total':total})
        
        
            
            
            
            
            
            
        

