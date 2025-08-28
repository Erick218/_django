from django.db import models

from django.contrib.auth.models import User

class UsuarioDados(models.Model):
    nome = models.CharField(
        max_length=150,
        verbose_name="Nome"
    )
    
    imagem = models.models.models.ImageField(
        _(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefere não dizer'),
    ]

    email = models.EmailField(
        verbose_name="E-mail"
    )

    cpf = models.CharField(
        max_length=14,  # Ajuste conforme o formato com ou sem pontos
        verbose_name="CPF"
    )

    tel_fixo = models.CharField(
        max_length=15,
        verbose_name="Telefone Fixo",
        blank=True,
        null=True
    )

    tel_celular = models.CharField(
        max_length=15,
        verbose_name="Telefone Celular",
        blank=True,
        null=True
    )

    data_nascimento = models.DateField(
        max_length=10,
        verbose_name="Data de Nascimento (DD/MM/AAAA)"
    )

    genero = models.CharField(
        max_length=1,
        choices=GENERO_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.email
