from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150,unique=True,verbose_name='Название')
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'category' # db_table имя таблицы / setting LANGUAGE_CODE = 'en-us' поменять на rus  тогда актуально весь код ниже так как админ панель будет на русском
        verbose_name = 'Категорию' # данная строчка в админ панеле отображет альтернотивное имя по моему желанию
        verbose_name_plural = 'Категории' # делает множественное число что то для програмирования и стандартов. мне пока все равно
        
    def __str__(self): #делаем этот метод что бы в админ анели не отаброжалось Categories Objects(1) а был красивый вывод привязанный к имени "Катигория"
        return self.name
        
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True,verbose_name='Название')
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images',blank=True,null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='цена')
    discount = models.DecimalField(default=0.00,max_digits=4,decimal_places=2,verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0,verbose_name='Количество')
    
    # нужно связать табицы: Product and Categories для этого создаем: models.ForeignKey  получаем значения из другой таблицы
    # 'to=Categories' свзываем с нужно таблицей
    # on_delete удалить категорию и все связаные товары, или запетитиь удаление категории или...
    # .Cascade при удалении категории удоляються все товары которые были закреплены. Через Админ панель будет предупрежление при удалении что если мы удалим то все товары из категории удаляться
    # .Protect если на категорию привязаны товары то ее не получиться удалить
    # .Set_Defoult при удалении категории все товаром будет присвоено значени по дефолту. его нужно указать через  default='значение'
    category = models.ForeignKey(to=Categories,on_delete=models.CASCADE, verbose_name='Категория')
    
    
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self): # для красивого отоброжения привязанного к имнеи
        return f"{self.name} Колличество - {self.quantity}"
    
    # метод для генерации ID для товара
    def display_id(self):
        return f"{self.id:05}"
    
    # метод для скидки. берет основную сумму, смотрит есть ли скидка если нет продаем self.price, если скидак стоит то ставим новую цену.
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        return self.price