# Generated by Django 5.0.6 on 2024-11-27 01:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_shoppost_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppost',
            name='bookmarked_by',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_products', to=settings.AUTH_USER_MODEL),
        ),
    ]