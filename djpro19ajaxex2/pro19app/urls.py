from django.urls import path
from pro19app.views import view1, view2

urlpatterns = [
    path("burger",view1.listFunc),
    path("drink",view1.list2Func),
    
    path("admin",view2.adminFunc),
    path("productadmin",view2.listFunc),
    path('productadd', view2.insertFunc),
]