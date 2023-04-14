# Generated by Django 4.2 on 2023-04-14 14:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Diaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.DateTimeField()),
                ('diaper', models.IntegerField(choices=[(1, 'Wet 💦'), (2, 'Dirty 💩')], default=1)),
                ('rash', models.BooleanField()),
                ('notes', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.DateTimeField()),
                ('amount', models.PositiveIntegerField()),
                ('method', models.IntegerField(choices=[(1, 'Bottle'), (2, 'Breast')], default=1)),
                ('notes', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('gender', models.IntegerField(choices=[(1, 'Boy'), (2, 'Girl')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babybliss.user')),
            ],
        ),
    ]
