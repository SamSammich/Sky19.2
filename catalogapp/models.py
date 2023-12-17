from django.db import models

NULLABLE = {
    'blank': True, 'null': True
}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.CharField(max_length=250, verbose_name='description')
    avatar = models.ImageField(upload_to='product/', verbose_name='avatar', **NULLABLE)
    category = models.PositiveIntegerField(verbose_name='category', **NULLABLE)
    price_for_one = models.PositiveIntegerField(verbose_name='price_for_one')
    date_of_creation = models.DateField(verbose_name='date_of_creation', **NULLABLE)
    last_change_date = models.DateField(verbose_name='last_change_date', **NULLABLE)
    is_available = models.BooleanField(default=True, verbose_name='available')

    views_count = models.PositiveIntegerField(default=0, verbose_name="Views")
    is_published = models.BooleanField(default=True, verbose_name='published')
    slug = models.CharField(max_length=150, verbose_name='slug',**NULLABLE )

    def __str__(self):
        return f'{self.name}: {self.category}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('date_of_creation',)

