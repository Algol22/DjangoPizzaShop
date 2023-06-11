from django.db import models

# Create your models here.

class PizzaShop(models.Model):
    name = models.CharField (max_length=30, verbose_name='Пиччя')
    description = models.TextField (verbose_name='Оисaние')
    rating = models.FloatField(default=0, verbose_name='PейTинг' )
    url = models. URLField (verbose_name='Интернет-адрес')

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Hазвание пиы')
    short_description = models.CharField(max_length=30, verbose_name='Kpаткое описание')
    price = models.IntegerField(default=0, verbose_name='чeнa')
    photo = models.ImageField('Photo', upload_to='firstapp/photos', default='', blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, verbose_name='Пиччa', on_delete=models.ForeignKey)
    name = models.CharField(max_length=30, verbose_name='ИMя')
    phone = models.CharField(max_length=30, verbose_name='Тeле☀он')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Ãa¹a')