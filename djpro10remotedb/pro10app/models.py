from django.db import models

# Create your models here.
class Guest(models.Model): #한결같음
    # myno = models.AutoField(auto_created=True,primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    regdate=models.DateTimeField()
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        # ordering=('title') #튜플 타입으로 기술
        ordering=('-id',)
        