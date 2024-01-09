from django.shortcuts import render
from pro21app.models import Jikwon
from django.http.response import HttpResponse
import json
from django.utils import timezone
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score,explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    dates = int(request.GET['dates'])  # 근무 년수
    jikwon=Jikwon.objects.all()
    datas=dates
    print(jikwon['jikwon_pay'])
    print()
    print(jikwon['jikwon_ibsail'])
  
    return HttpResponse(json.dumps(datas), content_type='application/json')
