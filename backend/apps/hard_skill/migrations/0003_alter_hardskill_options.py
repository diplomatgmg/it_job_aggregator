# Generated by Django 5.0.7 on 2024-08-20 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hard_skill", "0002_hardskill_ordering"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hardskill",
            options={"ordering": ("ordering", "name")},
        ),
    ]