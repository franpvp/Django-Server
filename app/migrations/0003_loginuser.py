# Generated by Django 4.1.7 on 2023-05-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_confirmarreserva_nombre_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='Nombre de Usuario')),
                ('password', models.CharField(max_length=30, verbose_name='Contraseña Usuario')),
            ],
        ),
    ]
