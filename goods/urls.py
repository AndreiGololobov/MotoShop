
from django.urls import path
from goods import views

app_name = 'goods'


urlpatterns = [

    
    path('',views.catalog, name='index'),
    
    #url диспатчер делаю конвертер int для url адресов чтобы не прописывать каждую ссылку отдельно для товаров
    path('product/<slug:product_slug>/',views.product, name='product'),

]
