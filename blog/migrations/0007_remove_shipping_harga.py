# Generated by Django 4.0.4 on 2022-05-11 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tarifperkilo_create_at_alter_shipping_harga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='harga',
        ),
    ]