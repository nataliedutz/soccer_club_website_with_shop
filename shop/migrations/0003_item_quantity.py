# Generated by Django 5.0.1 on 2024-02-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
