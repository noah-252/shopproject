# Generated by Django 5.0.6 on 2024-11-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_shoppost_condition_shoppost_day_shoppost_ken'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppost',
            name='price',
            field=models.CharField(default=' ', max_length=10, verbose_name='商品の値段'),
        ),
    ]
