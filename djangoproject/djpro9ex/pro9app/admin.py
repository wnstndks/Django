from django.contrib import admin
from pro9app.models import Friend

# Register your models here.
class FriendAdmin(admin.ModelAdmin):
    list_display=('irum','juso','nai') 
    

admin.site.register(Friend,FriendAdmin)