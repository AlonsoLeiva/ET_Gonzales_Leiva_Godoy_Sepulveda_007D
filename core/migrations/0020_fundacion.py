# Generated by Django 4.0.4 on 2022-06-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_rename_fecha_efetuada_producto_fecha_efectuada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100, verbose_name='Nombre de Usuario')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña')),
            ],
        ),
    ]