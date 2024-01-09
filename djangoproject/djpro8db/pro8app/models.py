from django.db import models

# Create your models here.
# jpa로 보면 entity라고 볼수 있다.-물리적인 테이블이 아님 논리적인 테이블을 클래스로 정의한 것 모든 rdbms는 바뀌어도 코드는 바뀌지 않음, 세팅설정에서만 바꾸어주면 된다.

class Article(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    pub_date=models.DateTimeField()
    
    # table은 primarykey인데 안줬음 ->migration을 할때 장고는 자동으로 auto field를 만들어준다. primary키로 자동증가하게 만듬

