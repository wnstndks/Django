from django.shortcuts import render, redirect
from pro21app.models import Survey
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')

# Create your views here.
def surveyMain(request):
    return render(request,'main.html')

def surveyView(request):
    return render(request,'survey.html')

def surveyProcess(request):
    insertData(request) #설문조사 결과를 DB에 저장
    return redirect('/coffee/surveyshow') #분석 결과 보기

def surveyAnalysis(request): # 이원카이제곱검정
    rdata = list(Survey.objects.all().values())
    # print(rdata)
    df=pd.DataFrame(rdata)
    df.dropna()
    # print(df)
    
    #남,녀를 1,2처럼 더미화해도 되고, 안하고 그냥 처리해도 가능하다.
    ctab=pd.crosstab(index=df['gender'],columns=df['co_survey'])
    
    # chi2 추정 및 검정
    chi, pv, _, _ = stats.chi2_contingency(observed=ctab)
    print('chi:{}, pv:{}'.format(chi,pv))
    
    if pv>=0.05:
        result="p값이 {0} >0.05이므로 <br>성별과 커피 브랜드의 선호도는 관계가 없다.(귀무채택)".format(pv)
    else:
        result="p값이 {0} <0.05이므로 <br>성별과 커피 브랜드의 선호도는 관계가 있다.(귀무채택)".format(pv)
    
    count=len(df)
    
    fig=plt.gcf()
    coffee_group=df.groupby(['co_survey'])['rnum'].count()
    coffee_group.plot.bar(color=['red','blue'],width=0.5, rot=0)
    plt.xlabel('커피 브랜드명')
    plt.title('커피 브랜드별 선호건수')
    plt.grid()
    fig.savefig('djpro21chi2_coffee/pro21app/static/images/coffee.png')
    
    return render(request,'list.html',{'ctab':ctab.to_html(), 'result':result, 'count':count})
    

def insertData(request):
    if request.method=='POST':
        # print(request.POST.get('gender'))
        # print(request.POST.get('age'))
        # print(request.POST.get('co_survey'))
        Survey(
            gender=request.POST.get('gender'),
            age=request.POST.get('age'),
            co_survey=request.POST.get('co_survey'),
        ).save()

        


    
