from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.CharField(max_length=250, verbose_name='description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
