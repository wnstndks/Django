from django.shortcuts import render
from useapp.models import Jikwon
import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    queryset = Jikwon.objects.order_by('buser_num', 'jikwon_name')
    df = pd.DataFrame(list(queryset.values()))
    jikwon={'df':df.to_html()}
    return render(request, 'list.html', jikwon)

def CalFunc(request):
    queryset = Jikwon.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    # 부서별 연봉 합 구하기
    df['jikwon_pay'] = df['jikwon_pay'].astype(float)  # 연봉을 숫자형으로 변환
    busersum = df.groupby('buser_num')['jikwon_pay'].sum()
    # 부서별 연봉 평균 구하기
    buavg = df.groupby('buser_num')['jikwon_pay'].mean()
    # 직급별 연봉 합 구하기
    jiksum = df.groupby('jikwon_jik')['jikwon_pay'].sum()
    # 직급별 연봉 평균 구하기
    jikavg = df.groupby('jikwon_jik')['jikwon_pay'].mean()
    
    context = {
        'busersum': busersum.to_frame().to_html(),
        'buavg': buavg.to_frame().to_html(),
        'jiksum': jiksum.to_frame().to_html(),
        'jikavg': jikavg.to_frame().to_html(),
    }

    return render(request, 'cal.html', context)

#부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
def GraphFunc(request):
    queryset = Jikwon.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    # 부서별 연봉 합 구하기
    df['jikwon_pay'] = df['jikwon_pay'].astype(float)  # 연봉을 숫자형으로 변환
    busersum = df.groupby('buser_num')['jikwon_pay'].sum()
    # 부서별 연봉 평균 구하기
    buavg = df.groupby('buser_num')['jikwon_pay'].mean()
   
   
    context = {
        'busersum': busersum.to_frame().to_html(),
        'buavg': buavg.to_frame().to_html(),
    }

    return render(request, 'graph.html')


def TableFunc(request):
    pass

