# Generated by Django 4.0.4 on 2022-05-11 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_shipping_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarifperkilo',
            name='harga',
            field=models.CharField(max_length=10),
        ),
    ]
