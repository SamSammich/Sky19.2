# Generated by Django 5.0 on 2023-12-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0004_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='product',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Views'),
        ),
    ]
