# Generated by Django 5.0.6 on 2024-07-03 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('format', models.CharField(choices=[('r', 'Удаленка'), ('o', 'Офис'), ('h', 'Гибрид')], max_length=16)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.company')),
                ('grades', models.ManyToManyField(related_name='vacancies', to='job.grade')),
                ('hard_skills', models.ManyToManyField(related_name='jobs', to='job.hardskill')),
            ],
        ),
    ]
