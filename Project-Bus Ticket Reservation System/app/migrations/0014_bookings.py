# Generated by Django 3.0.8 on 2020-08-08 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200809_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromplace', models.CharField(max_length=20)),
                ('toplace', models.CharField(max_length=20)),
                ('noofseats', models.IntegerField()),
                ('category', models.CharField(max_length=30)),
                ('depart', models.CharField(max_length=10)),
                ('fare', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Fun')),
            ],
        ),
    ]
