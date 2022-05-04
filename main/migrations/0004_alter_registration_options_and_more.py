# Generated by Django 4.0.3 on 2022-04-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_registration_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['name'], 'verbose_name': 'Регистрация', 'verbose_name_plural': 'Регистрация'},
        ),
        migrations.AddConstraint(
            model_name='registration',
            constraint=models.CheckConstraint(check=models.Q(('title__length__gte', 1)), name='main_registration_title_length'),
        ),
    ]
