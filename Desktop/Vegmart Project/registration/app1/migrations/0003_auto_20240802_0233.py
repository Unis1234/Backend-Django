# Generated by Django 3.0.5 on 2024-08-01 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='commercial',
        ),
        migrations.DeleteModel(
            name='Domestic',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
