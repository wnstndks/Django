from django.urls import path
from views import view1, view2

urlpatterns = [
    path("list",view1.listFunc),
    path("insert",view1.insertFunc),
    path("search",view1.searchFunc),
    path("content",view1.contentFunc),
    path("update",view1.updateFunc),
    path("delete",view1.deleteFunc),
    
    #댓글은 view2에서
    path("reply",view2.replyFunc),
    path("replyok",view2.replyokFunc),
]