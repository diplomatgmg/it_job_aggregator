# Generated by Django 5.0.7 on 2024-07-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hard_skill', '0003_alter_unknownhardskill_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unknownhardskill',
            name='create_count',
            field=models.IntegerField(default=0),
        ),
    ]