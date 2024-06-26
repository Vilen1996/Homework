# Generated by Django 5.0.5 on 2024-05-07 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('address', models.CharField(default='Armenia', max_length=30)),
                ('photo', models.ImageField(upload_to='media/cars/')),
                ('draft', models.CharField(choices=[('Electric', 'Electric Urban Commuter'), ('Off-Road', 'Off-Road Adventure SUV'), ('Luxury', 'Luxury Autonomous Sedan'), ('Hybrid', 'Hybrid Family Crossover'), ('Performance', 'Performance Electric Sports Car')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('draft', models.CharField(choices=[('Electric', 'Electric Urban Commuter'), ('Off-Road', 'Off-Road Adventure SUV'), ('Luxury', 'Luxury Autonomous Sedan'), ('Hybrid', 'Hybrid Family Crossover'), ('Performance', 'Performance Electric Sports Car')], max_length=15)),
                ('colors', models.CharField(choices=[('silver', 'Silver'), ('white', 'White'), ('black', 'Black'), ('blue', 'Blue'), ('red', 'Red')], max_length=15)),
                ('photo', models.ImageField(upload_to='media/cars/')),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.manufacture')),
            ],
        ),
    ]
