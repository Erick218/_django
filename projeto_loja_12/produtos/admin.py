# produtos/admin.py - Aula 11

from django.contrib import admin

# Importa o modelo Produto da sua aplicação (Aula 11)
# from .models import Produto 

# Importa os modelos da aplicação produto (Aula 12.02.03)
from .models import Categoria, Produto


# Registra o modelo Produto - Aula 11 parte 01
#admin.site.register(Produto)

# Define uma classe ModelAdmin para o modelo Produto (Aula 11)
class ProdutoAdmin(admin.ModelAdmin):
    
    # Campos que serão exibidos na página de lista de objetos (Aula 11 e 12)
    list_display = ('nome', 'categoria', 'preco', 'estoque', 'disponivel')
    
    # Campos que podem ser clicados para ordenar a lista (Aula 11)
    list_display_links = ('nome',)
    
    # Adiciona uma barra lateral de filtro para os campos (Aula 11 e 12)
    list_filter = ('disponivel', 'data_criacao', 'categoria') 
    
    # Adiciona uma barra de pesquisa
    search_fields = ('nome', 'descricao') # Pesquisa por nome ou descrição
    
    # Permite editar campos diretamente na lista (cuidado com isso em produção!)
    list_editable = ('preco', 'estoque', 'disponivel')
    
    # Pre-popula o campo 'slug' (se você tiver um) baseado no 'nome' (Aula 11)
    # prepopulated_fields = {'slug': ('nome',)}
    
    # Agrupa campos no formulário de edição/criação (Aula 11)
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem')
        }),
    )

# Registra o modelo Produto com a sua classe ModelAdmin personalizada (Aula 11)
admin.site.register(Produto, ProdutoAdmin)

# Registra o modelo Categoria - Aula 12.02.03
admin.site.register(Categoria)
