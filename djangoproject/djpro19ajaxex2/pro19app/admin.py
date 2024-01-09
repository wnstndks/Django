from django.contrib import admin
from pro19app.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','category','pname','price','stock','description')
    
admin.site.register(Product,ProductAdmin)