# Generated by Django 5.0.6 on 2024-07-15 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("company", "0001_initial"),
        ("grade", "0001_initial"),
        ("hard_skill", "0001_initial"),
        ("profession", "0001_initial"),
        ("work_format", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "unique_hash",
                    models.CharField(
                        blank=True,
                        editable=False,
                        max_length=32,
                        null=True,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("salary_from", models.IntegerField(blank=True, null=True)),
                ("salary_to", models.IntegerField(blank=True, null=True)),
                ("experience", models.CharField(max_length=255)),
                ("url", models.URLField()),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.company",
                    ),
                ),
                (
                    "grade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="grade.grade"
                    ),
                ),
                (
                    "hard_skills",
                    models.ManyToManyField(
                        related_name="vacancies", to="hard_skill.hardskill"
                    ),
                ),
                (
                    "profession",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profession.profession",
                    ),
                ),
                (
                    "work_formats",
                    models.ManyToManyField(
                        related_name="vacancies", to="work_format.workformat"
                    ),
                ),
            ],
        ),
    ]
