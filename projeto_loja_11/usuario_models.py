class Usuario_dados(models.Model):
    nome = models.CharField(
        max_length=150, 
        verbose_name="Nome"
        )
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
        verbose_name="CPF"
    )
    
    tel_fixo = models.CharField(
        verbose_name="(XX)XXXXX-XXXX"
        blank=True
    )

    tel_celular = models.CharField(
        verbose_name="(XX)XXXXX-XXXX"
        blank=True
    )

    data_nascimento = models.Charfield(
        verbose_name="XX/XX/XXXX"
    )

    genero = models.CharField (
        max_length=1
        choices=GENERO_CHOICES,
        blank=True
        null=True
    )