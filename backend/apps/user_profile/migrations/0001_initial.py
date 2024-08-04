# Generated by Django 5.0.7 on 2024-08-04 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grade', '0001_initial'),
        ('hard_skill', '0001_initial'),
        ('profession', '0001_initial'),
        ('work_format', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('grades', models.ManyToManyField(blank=True, related_name='profiles', to='grade.grade')),
                ('hard_skills', models.ManyToManyField(blank=True, related_name='profiles', to='hard_skill.hardskill')),
                ('professions', models.ManyToManyField(blank=True, related_name='profiles', to='profession.profession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_formats', models.ManyToManyField(blank=True, related_name='profiles', to='work_format.workformat')),
            ],
        ),
    ]
