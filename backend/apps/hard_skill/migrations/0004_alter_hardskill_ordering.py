# Generated by Django 5.0.7 on 2024-08-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hard_skill", "0003_alter_hardskill_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hardskill",
            name="ordering",
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
    ]
