from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Nombre de la categoria',max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products', on_delete = models.CASCADE)
    name = models.CharField('Nombre',max_length=200, db_index=True)
    slug = models.SlugField('Slug',max_length=200, db_index=True)
    image = models.ImageField('Imangen',upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('Descripcion',blank=True)
    price = models.DecimalField('Preci',max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('En stock')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
