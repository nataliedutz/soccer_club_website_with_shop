# Generated by Django 5.0.1 on 2024-03-06 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('shop', '0005_remove_order_user_order_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
