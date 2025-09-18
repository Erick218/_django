# produtos/models.py (aula 10)

from django.db import models

##
# Primeira versão do model adicionado na aula 10
##
# class Produto(models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.TextField()
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) # Campo para imagem

#     def __str__(self):
#         return self.nome


##
# Modelo - Categoria (Aula 11.02.02) (Aula 12.02.02)
##
class Categoria(models.Model):
    nome = models.CharField(max_length=100, 
        verbose_name="Nome da Categoria", 
        unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


##
# Aula 11 - 11.01.01
##
class Produto(models.Model):
    nome = models.CharField(
        max_length=100, 
        help_text="Nome do produto"
        )
    
    descricao = models.TextField(
        help_text="Descrição detalhada do produto"
        )
    
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Preço de venda do produto"
    )
    
    estoque = models.PositiveIntegerField(
        default=0, 
        help_text="Quantidade do produto em estoque"
    )

    disponivel = models.BooleanField(
        default=True, 
        help_text="Indica se o produto está disponível para venda"
    )
    
    imagem = models.ImageField(
        upload_to='produtos/', 
        blank=True, 
        null=True, 
        help_text="Imagem de exibição do produto"
    )



    # Campos de data
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
   

    # Aqui está a relação! Cada produto pertence a uma categoria. (Aula 11.02.02)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,  # <-- Permite que o valor no banco de dados seja NULO
        blank=True, # <-- Permite que o campo no admin/formulários fique em branco 
        related_name="produtos")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']


