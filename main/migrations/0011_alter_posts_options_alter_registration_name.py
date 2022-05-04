# Generated by Django 4.0.3 on 2022-04-28 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_phonenumber_registration_telnumber_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={},
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[a-zA-Z1-10]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]