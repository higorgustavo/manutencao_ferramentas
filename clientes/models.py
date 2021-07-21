from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Cliente")
    codigo_ciss = models.IntegerField(unique=True, null=True, blank=True, verbose_name="Código no CISS")
    telefone1 = models.IntegerField(verbose_name="Telefone Principal")
    telefone2 = models.IntegerField(null=True, blank=True, verbose_name="Telefone Reserva (opcional)")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome', ]
        db_table = 'clientes'

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        return super(Cliente, self).save()

    def __str__(self):
        return self.nome
