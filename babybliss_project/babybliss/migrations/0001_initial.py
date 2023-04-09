# Generated by Django 4.2 on 2023-04-09 22:07

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
                ('date', models.DateField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
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
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('amount', models.IntegerField()),
                ('breastFed', models.BooleanField()),
                ('bottleFed', models.BooleanField()),
                ('notes', models.TextField()),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babybliss.baby')),
            ],
        ),
        migrations.CreateModel(
            name='Diaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('wet', models.BooleanField()),
                ('dirty', models.BooleanField()),
                ('rash', models.BooleanField()),
                ('notes', models.TextField()),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babybliss.baby')),
            ],
        ),
        migrations.AddField(
            model_name='baby',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babybliss.user'),
        ),
    ]
