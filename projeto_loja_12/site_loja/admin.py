# site_loja/admin.py - Aula 10

from django.contrib import admin

# Aula 11s
#from .models import Perfil 

# Aula 12.02.03
from .models import Perfil, Contato, Comentario, Compra, ItemCompra

# Registra o model - Perfil - Aula 11
admin.site.register(Perfil)

# Registra o model - Contato - Aula 12.02.03
#admin.site.register(Contato)

# Registra o model - Contato - Aula 12.02.04
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    """
    Personalização da exibição do modelo Contato.
    """
    
    # list_display para ver rapidamente as informações essenciais
    list_display = ('nome', 'email', 'assunto', 'data_criacao', 'lido')
    
    # search_fields para encontrar uma mensagem pelo nome, email ou assunto
    search_fields = ('nome', 'email', 'assunto')
    
    # list_filter para separar mensagens lidas das não lidas
    list_filter = ('lido', 'data_criacao')

# Registra o model - ItemCompra - Aula 12.02.03
#admin.site.register(ItemCompra)

# Criamos uma classe Inline para ItemCompra (Aula 12.02.04)
class ItemCompraInline(admin.TabularInline):
    """
    Define o formato de exibição dos Itens de Compra dentro da página de Compra.
    TabularInline exibe os itens em um formato de tabela compacto.
    """
    model = ItemCompra  # O modelo que será exibido
    extra = 1  # Quantos formulários em branco para novos itens serão exibidos

# Registra o model - Compra - Aula 12.02.03
#admin.site.register(Compra)

#  (Aula 12.02.04)
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    """
    Personalização da exibição do modelo Compra.
    """
    list_display = ('id', 'cliente', 'data_compra', 'status', 'valor_total')
    list_filter = ('status', 'data_compra')
    search_fields = ('cliente__username', 'id')
    
    # Adicionamos o inline definido acima à página de administração de Compra
    inlines = [ItemCompraInline]

    def valor_total(self, obj):
        """
        Um método customizado para exibir o valor total da compra na lista.
        """
        return f"R$ {obj.get_total()}"
    
    # Define um nome amigável para a coluna no admin
    valor_total.short_description = 'Total da Compra'

# Registra o model - Comentario - Aula 12.02.03
admin.site.register(Comentario)



