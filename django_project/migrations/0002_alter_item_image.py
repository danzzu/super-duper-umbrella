# Generated by Django 5.0.2 on 2024-09-30 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
