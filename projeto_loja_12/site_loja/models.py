# site_loja/models.py
from django.db import models

# Importa o modelo de usuário padrão do Django
from django.contrib.auth.models import User 

# Importa o Image para redimensionar a imagem
from PIL import Image                       

# Importando o modelo Produto da outra aplicação (Aula 12.02.02)
from produtos.models import Produto

##
# Perfil do usuário
##
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Salva a imagem primeiro

        img = Image.open(self.imagem.path) # Abre a imagem
        if img.height > 300 or img.width > 300: # Verifica se é maior que 300x300 pixels
            output_size = (300, 300)
            img.thumbnail(output_size) # Redimensiona a imagem
            img.save(self.imagem.path) # Salva a imagem redimensionada

##
# Modelo - Contatos (Aula 11.02.02) (Aula 12.02.02)
##
class Contato(models.Model):
    nome = models.CharField(
        max_length=150, 
        verbose_name="Nome"
        )
    
    email = models.EmailField(
        verbose_name="E-mail"
        )
    
    assunto = models.CharField(
        max_length=150,
        default='Sem assunto', 
        blank=True 
        )
    
    mensagem = models.TextField(
        verbose_name="Mensagem"
        )
    
    # Campos de data
    data_criacao = models.DateTimeField(
        auto_now_add=True
        )
    
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
        verbose_name="Enviado em"
        )
    
    lido = models.BooleanField(
        default=False, 
        help_text="Marca se a mensagem foi lida"
        )

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_criacao']

##
# Modelo - Comentário (Aula 12.02.02)
##
class Comentario(models.Model):
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )

    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )

    texto = models.TextField()

    data_publicacao = models.DateTimeField(auto_now_add=True)

    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.produto.nome}'

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ['-data_publicacao']

##
# Modelo - Compra (Aula 12.02.02)
##
class Compra(models.Model):
    class StatusCompra(models.TextChoices):
        PAGAMENTO_PENDENTE = 'Pendente', 'Pagamento Pendente'
        PROCESSANDO = 'Processando', 'Processando'
        ENVIADO = 'Enviado', 'Enviado'
        ENTREGUE = 'Entregue', 'Entregue'
        CANCELADO = 'Cancelado', 'Cancelado'

    cliente = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        related_name='compras'
    )
    
    data_compra = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=StatusCompra.choices,
        default=StatusCompra.PAGAMENTO_PENDENTE
    )
    
    def __str__(self):
        return f'Compra #{self.id} - {self.cliente.username}'
    
    # Esta função calcularia o total da compra
    def get_total(self):
        total = sum(item.get_custo() for item in self.itens.all())
        return total

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['-data_compra']

##
# Modelo - Intem da Compra (Aula 12.02.02)
##
class ItemCompra(models.Model):
    compra = models.ForeignKey(
        Compra, 
        on_delete=models.CASCADE, 
        related_name='itens'
    )

    produto = models.ForeignKey(
        Produto, 
        on_delete=models.PROTECT, 
        related_name='itens_comprados'
    )

    preco_unitario = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome} na Compra #{self.compra.id}'
    
    # Esta função calcula o custo deste item (preço x quantidade)
    def get_custo(self):
        return self.preco_unitario * self.quantidade

    class Meta:
        verbose_name = "Item de Compra"
        verbose_name_plural = "Itens de Compra"