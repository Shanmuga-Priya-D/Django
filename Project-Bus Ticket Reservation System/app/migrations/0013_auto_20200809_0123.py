# Generated by Django 3.0.8 on 2020-08-08 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_search_us'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Bus',
        ),
    ]
