# Generated by Django 4.0.6 on 2022-08-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panificacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='panes',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='panes',
            name='sku',
            field=models.IntegerField(default=782),
        ),
    ]
