# Generated by Django 4.0.4 on 2022-06-18 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_rename_fecha_expira_producto_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreproducto', models.CharField(max_length=100, verbose_name='Nombre Producto')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('precio', models.IntegerField(verbose_name='Precio')),
            ],
        ),
    ]