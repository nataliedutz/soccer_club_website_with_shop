# Generated by Django 5.0.1 on 2024-01-19 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_remove_player_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='team.player'),
        ),
    ]
