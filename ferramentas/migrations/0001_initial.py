# Generated by Django 2.2.4 on 2021-08-08 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome da ferramenta')),
                ('numero_serie', models.CharField(blank=True, max_length=100, null=True, verbose_name='Número de série')),
                ('data_compra', models.DateField(blank=True, null=True, verbose_name='Data de compra')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações sobre a ferramenta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente')),
            ],
            options={
                'verbose_name': 'Ferramenta',
                'verbose_name_plural': 'Ferramentas',
                'db_table': 'ferramentas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_manutencao', models.DateField(verbose_name='Data da Manutenção')),
                ('status_manutencao', models.CharField(choices=[['Agendada', 'Agendada'], ['Atrasada', 'Atrasada'], ['Cancelada', 'Cancelada'], ['Concluída', 'Concluída']], max_length=25, verbose_name='Status da Manutenção')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações (opicional)')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor da Manutenção')),
                ('numero_os', models.IntegerField(blank=True, null=True, verbose_name='Número da Ordem se Serviço')),
                ('ferramenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ferramentas.Ferramenta')),
            ],
            options={
                'verbose_name': 'Manutenção',
                'verbose_name_plural': 'Manutenções',
                'db_table': 'manutencoes',
                'ordering': ['-data_manutencao'],
            },
        ),
    ]
