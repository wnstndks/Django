from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def DispFunc(request):
    q_list=Question.objects.all().order_by('pub_date','id')
    context ={'q_list': q_list}
    return render(request, 'display.html',context)
    
def DetailFunc(request, question_id):
    print('question_id : ',question_id)
    # try:
    #     question=Question.objects.get(pk=question_id)
    #
    # except Question.DoesNotExist:
    #     raise Http404("질문 항목 파일이 없음.")
    
    # get_object_or_404 : 장고에서는 없는 페이지에 대한 요청이 들어왔을 경우 404 오류를 발생시켜주는 메소드
    question=get_object_or_404(Question,pk=question_id)
    print(question.question_text)
    print(question.pub_date)
    print(question)
    print('question.choice_set.all : ',question.choice_set.all)
    
    for cho in question.choice_set.all():
        print(cho.choice_text)
        
    return render(request, 'detail.html',{'question':question})

def VoteFunc(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'err_msg':'1개의 항목을 선택하세요'})

    sel_choice.votes += 1
    sel_choice.save()   # 선택 항목을 1씩 증가 후 테이블 수정
    print(reverse('results', args=(question.id,)))   # tuple type -> , 빼먹지말기

    return HttpResponseRedirect(reverse('results', args=(question.id,)))

def ResultFunc(request, question_id):
    # return HttpResponse("bb")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question':question})
    