from django.contrib import admin
from pro8app.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','code','name','price','pub_date') #자기가 보고 싶은 컬럼 여기에 쓰기
    

admin.site.register(Article,ArticleAdmin)#자료들을 추가하는 것
