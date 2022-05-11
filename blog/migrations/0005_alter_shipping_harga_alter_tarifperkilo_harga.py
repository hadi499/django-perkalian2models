# Generated by Django 4.0.4 on 2022-05-11 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_tarifperkilo_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='harga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tarifperkilo'),
        ),
        migrations.AlterField(
            model_name='tarifperkilo',
            name='harga',
            field=models.CharField(max_length=100),
        ),
    ]
