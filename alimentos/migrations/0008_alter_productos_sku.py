# Generated by Django 4.0.6 on 2022-08-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0007_alter_productos_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='sku',
            field=models.IntegerField(default=893),
        ),
    ]
