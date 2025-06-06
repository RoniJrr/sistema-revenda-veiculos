from django.db import models

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    quilometragem = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fipe = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    vendido = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição detalhada')


    destaque = models.BooleanField(default=False)  # <-- novo campo para destaque

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"