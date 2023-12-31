# Generated by Django 5.0 on 2023-12-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=250, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='avatar')),
                ('category', models.PositiveIntegerField(blank=True, null=True, verbose_name='category')),
                ('price_for_one', models.PositiveIntegerField(verbose_name='price_for_one')),
                ('date_of_creation', models.DateField(blank=True, null=True, verbose_name='date_of_creation')),
                ('last_change_date', models.DateField(blank=True, null=True, verbose_name='last_change_date')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('date_of_creation',),
            },
        ),
    ]
