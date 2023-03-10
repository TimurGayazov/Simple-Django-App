# Generated by Django 3.2.16 on 2023-02-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=10, verbose_name='Номер чека')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('price', models.FloatField(max_length=6, verbose_name='Цена')),
                ('product_name', models.CharField(max_length=50, verbose_name='Название товара')),
            ],
        ),
    ]
