from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product) 
admin.site.register(Weight)
admin.site.register(Ingredient)
admin.site.register(Addon)
admin.site.register(Category)