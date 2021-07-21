from django.db import models
from clientes.models import Cliente


class Ferramenta(models.Model):
    nome = models.CharField(max_length=200)
    serie = models.CharField(max_length=100, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_compra = models.DateField(null=True, blank=True, verbose_name="Data de compra")

    class Meta:
        verbose_name = 'Ferramenta'
        verbose_name_plural = 'Ferramentas'
        ordering = ['nome', ]
        db_table = 'ferramentas'

    def __str__(self):
        return self.nome + " - " + self.serie


class Manutencao(models.Model):

    STATUS = [
        ["Agendada", "Agendada"],
        ["Atrasada", "Atrasada"],
        ["Cancelada", "Cancelada"],
        ["Concluída", "Concluída"],
    ]

    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.CASCADE)
    data_manutencao = models.DateField(verbose_name="Data da Manutenção")
    status_manutencao = models.CharField(max_length=25, choices=STATUS, verbose_name="Status da Manutenção")
    # data_prox_manutencao = models.DateField(null=True, blank=True, verbose_name="Data da próxima Manutenção")
    observacoes = models.TextField(verbose_name="Observações da Manutenção", null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                verbose_name="Valor da Manutenção")
    numero_os = models.IntegerField(verbose_name="Número da Ordem se Serviço", null=True, blank=True)

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'
        ordering = ['-data_manutencao', ]
        db_table = 'manutencoes'

    def __str__(self):
        return self.ferramenta.nome + " - " + self.ferramenta.serie + " - " + str(self.data_manutencao)
