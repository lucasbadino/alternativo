# Generated by Django 4.0.6 on 2022-08-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panificacion', '0004_alter_panes_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panes',
            name='sku',
            field=models.IntegerField(default=597),
        ),
    ]
