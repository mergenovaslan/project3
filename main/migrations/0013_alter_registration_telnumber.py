# Generated by Django 4.0.3 on 2022-04-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_postes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='telnumber',
            field=models.IntegerField(unique=True),
        ),
    ]