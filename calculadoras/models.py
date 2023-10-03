from django.db import models
from django.contrib.auth.models import User

class Inversion(models.Model):
    usuario = models.OneToOneField(User, related_name="consultas_inversiones", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    monto_a_invertir = models.DecimalField(max_digits=50, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=6, decimal_places=2)
    periodo = models.PositiveSmallIntegerField(help_text="Cantidad de meses")
    retorno_periodo = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    retorno_anual = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)

    def get_retorno_anual(self):
        tasa_decimal = self.tasa_interes / 100
        retorno_anual = tasa_decimal * self.monto_a_invertir
        return retorno_anual

    def get_retorno_periodo(self):
        retorno_anual = self.get_retorno_anual()
        retorno_periodo = (self.periodo * retorno_anual) / 12
        return retorno_periodo

    def save(self, *args, **kwargs):
        self.retorno_anual = self.get_retorno_anual()
        self.retorno_periodo = self.get_retorno_periodo()
        super().save(*args, **kwargs)
        
        
    def __str__ (self):
        return f'Consulta Inversión de {self.usuario.username} ({self.date.strftime("%d/%m/%Y %H:%M")})'

    class Meta:
        verbose_name_plural = "inversiones"

        verbose_name = "inversión"



class Prestamo(models.Model):
    usuario = models.OneToOneField(User, related_name="consultas_prestamos", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    monto_a_solicitar = models.DecimalField(max_digits=50, decimal_places=2)
    valor_cuota = models.DecimalField(max_digits=6, decimal_places=2)
    n_cuotas = models.PositiveSmallIntegerField(help_text="Número de cuotas")
    interes_mensual = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    interes_total = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)

    def get_interes_total(self):
        interes_total = (self.n_cuotas * self.valor_cuota) - self.monto_a_solicitar
        return interes_total

    def get_interes_mensual(self):
        interes_mensual = self.get_interes_total() / self.n_cuotas
        return interes_mensual

    def save(self, *args, **kwargs):
        self.interes_total = self.get_interes_total()
        self.interes_mensual = self.get_interes_mensual()
        super().save(*args, **kwargs)

    
    def __str__ (self):
        return f'Consulta Préstamo de {self.usuario.username} ({self.date.strftime("%d/%m/%Y %H:%M")})'
    
    
    
    class Meta:
        verbose_name_plural = "préstamos"
        verbose_name = "préstamo"