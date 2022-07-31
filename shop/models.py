from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

from cloudinary.models import CloudinaryField

class Category(models.Model):
    """ Категория товара на сайте (ложки, посуда)"""
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url_products(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def get_absolute_url_sales(self):
        return reverse('shop:product_list_sale_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Maker(models.Model):
    """ Производитель товаров """
    company = models.CharField(max_length=200, db_index=True)
    country = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_maker', args=[self.slug])

    class Meta:
        ordering = ('company',)
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.company


class Product(models.Model):
    """ Товар и его полное описание """
    category = models.ForeignKey(
                                Category,
                                verbose_name='Категория',
                                related_name='products',
                                on_delete=models.CASCADE
                                )
    name = models.CharField('Имя товара', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    maker = models.ForeignKey(
                                Maker,
                                verbose_name='Производитель',
                                related_name='products',
                                on_delete=models.CASCADE,
                                )
    SKU = models.CharField('Артикул', max_length=50, db_index=True)
    description = models.TextField('Описание', blank=True)
    # image = models.ImageField('Фото', upload_to='products/%Y/%m/%d', blank=True)
    image = CloudinaryField('Фото', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    sale = models.IntegerField('Скидка %', default=0, validators=[
                                            MaxValueValidator(100),
                                            MinValueValidator(0)
                                            ])
    on_sale = models.BooleanField('По акции', default=False)
    available = models.BooleanField('В наличии', default=True)
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    updated = models.DateTimeField('Изменен', auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def get_total_price(self):
        return self.price - (self.price * self.sale / 100)

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
