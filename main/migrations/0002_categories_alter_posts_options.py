# Generated by Django 4.0.3 on 2022-04-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('picture', models.ImageField(default='default value', upload_to='')),
                ('describe', models.TextField(default='DataFlair Django tutorials')),
            ],
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Тақырып', 'verbose_name_plural': 'Тақырыптар'},
        ),
    ]
