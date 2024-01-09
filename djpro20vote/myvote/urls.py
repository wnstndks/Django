from django.urls import path
from myvote import views

urlpatterns = [
    path('', views.DispFunc, name='disp'),  # go/ 요청이 그냥 gogo/일때 여기로,
    path('<int:question_id>', views.DetailFunc, name='detail'),   #id가 넘어옴, 타입과 키워드 인자명을 쓴다. , 인자 컨버터 - 형식: <type:name>, 순서는 타입을 적어두고 이름을 준다 / 인자 컨버터 <type:name>  go/1 or go/2
                                                    # url 요청별로 name을 줌, display에서 요청을 줄때 이름과 관련이 있다.
                                                    # gogo/1 또는 gogo/2이면 DetailFunc로
    path('<int:question_id>/vote/', views.VoteFunc, name='vote'),   # gogo 1또는 2가 넘어오는데 vote,go/1/vote 이런식으로 넘어 옴  / 질문 번호가 아니라 전체 목록에 번호임            
    path('<int:question_id>/results/', views.ResultFunc, name='results'),   # gogo한다음에 vote가 아니라 result,
]
