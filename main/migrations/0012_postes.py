# Generated by Django 4.0.3 on 2022-04-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_posts_options_alter_registration_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тақырып')),
                ('is_published', models.BooleanField(default=True, verbose_name='Шығарылым')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
    ]
