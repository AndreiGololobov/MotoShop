from django.contrib import admin
from goods.models import Categories,Products
# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Products)


# настройка админ панели что бы slug заполнялся автаматически
# передаем словарь {'slug'(,)} первое значит что нам нужно заполнить, второе = {'slug': ('name',)} name значит откуда и с какого поля мы берем инф
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Products)    
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    