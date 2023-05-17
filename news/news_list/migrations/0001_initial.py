# Generated by Django 3.2.19 on 2023-05-17 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название', max_length=30, verbose_name='Заголовок')),
                ('text', models.TextField(help_text='Введите текст', verbose_name='ТЕКСТ НОВОСТИ')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='help_date', verbose_name='ДАТА')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='news_images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
