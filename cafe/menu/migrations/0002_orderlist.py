# Generated by Django 4.1.6 on 2023-03-04 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('number', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('status_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
