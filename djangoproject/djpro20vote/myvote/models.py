from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.question_text #이게 아니었으면 admin에서 id가 나온다.

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    votes=models.IntegerField(default=0)
    
    