# Generated by Django 4.0.6 on 2022-08-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0003_productos_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='sku',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
