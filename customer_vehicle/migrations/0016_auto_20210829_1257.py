# Generated by Django 2.2 on 2021-08-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_vehicle', '0015_auto_20210829_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='purchase_date',
            field=models.DateField(blank=True, verbose_name='purchase_date(MM/dd/yyyy)'),
        ),
    ]
