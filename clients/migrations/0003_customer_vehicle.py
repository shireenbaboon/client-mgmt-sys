# Generated by Django 2.2 on 2021-08-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('make', models.CharField(default=' ', max_length=20)),
                ('model', models.CharField(default=' ', max_length=20)),
                ('vin_number', models.CharField(default=' ', max_length=20)),
                ('purchase_date', models.DateTimeField()),
                ('last_service_date', models.DateTimeField()),
            ],
        ),
    ]
