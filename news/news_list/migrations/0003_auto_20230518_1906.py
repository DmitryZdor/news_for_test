# Generated by Django 3.2.19 on 2023-05-18 12:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news_list', '0002_auto_20230518_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, help_text='дата опубликования', verbose_name='ДАТА'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=tinymce.models.HTMLField(help_text='Введите текст', verbose_name='ТЕКСТ НОВОСТИ'),
        ),
    ]
