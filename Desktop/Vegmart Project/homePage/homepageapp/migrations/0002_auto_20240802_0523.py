# Generated by Django 3.0.5 on 2024-08-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetable',
            name='image_url',
            field=models.URLField(max_length=500),
        ),
    ]
