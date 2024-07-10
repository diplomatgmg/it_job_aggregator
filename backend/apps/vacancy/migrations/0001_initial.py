# Generated by Django 5.0.6 on 2024-07-10 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('grade', '0001_initial'),
        ('hard_skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('format', models.CharField(choices=[('r', 'Удаленка'), ('o', 'Офис'), ('h', 'Гибрид')], max_length=16)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('grades', models.ManyToManyField(related_name='vacancies', to='grade.grade')),
                ('hard_skills', models.ManyToManyField(related_name='vacancies', to='hard_skill.hardskill')),
            ],
        ),
    ]
