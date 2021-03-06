# Generated by Django 4.0.4 on 2022-05-11 06:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_shipping_harga_alter_tarifperkilo_harga'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifperkilo',
            name='create_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipping',
            name='harga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.tarifperkilo'),
        ),
    ]
