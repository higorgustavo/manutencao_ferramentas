# Generated by Django 2.2.4 on 2021-08-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do Cliente')),
                ('codigo_ciss', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Código no CISS')),
                ('telefone1', models.IntegerField(verbose_name='Telefone Principal')),
                ('telefone2', models.IntegerField(blank=True, null=True, verbose_name='Telefone Reserva (opcional)')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'clientes',
                'ordering': ['nome'],
            },
        ),
    ]
