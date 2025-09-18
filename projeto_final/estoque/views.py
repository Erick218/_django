from django.shortcuts import render

class ProdutoListView(ProdutoListView):
    model = Produto
    template_name = 'estoque/produto_list.html'
    context_object_name = 'produtos'
    ordering = ['nome']