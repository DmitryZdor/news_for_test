# Generated by Django 3.2.19 on 2023-05-18 12:06

from django.db import migrations, models
import django_admin_geomap


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=255, verbose_name='Название места')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
    ]