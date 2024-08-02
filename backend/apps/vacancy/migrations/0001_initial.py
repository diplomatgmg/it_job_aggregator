# Generated by Django 5.0.7 on 2024-08-02 11:59

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('grade', '0001_initial'),
        ('hard_skill', '0001_initial'),
        ('profession', '0001_initial'),
        ('work_format', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_hash', models.CharField(editable=False, max_length=64, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_hash', models.CharField(editable=False, max_length=64, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('salary_from', models.IntegerField(blank=True, null=True)),
                ('salary_to', models.IntegerField(blank=True, null=True)),
                ('experience', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.grade')),
                ('hard_skills', models.ManyToManyField(related_name='vacancies', to='hard_skill.hardskill')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profession.profession')),
                ('work_formats', models.ManyToManyField(related_name='vacancies', to='work_format.workformat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_viewed', models.BooleanField(default=False)),
                ('suitability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.vacancy')),
            ],
            options={
                'unique_together': {('user', 'vacancy')},
            },
        ),
    ]
