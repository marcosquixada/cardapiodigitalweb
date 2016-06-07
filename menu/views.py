from rest_framework import permissions, viewsets, generics	
from rest_framework.response import Response
from menu.models import Item,Categoria,ItemPedido
from menu.serializers import PaginatedCardapioSerializer,ItemSerializer,PaginatedCategoriaSerializer,CategoriaSerializer
from django.shortcuts import render_to_response
from django.template import RequestContext,Context

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.order_by('-created_at')
    pagination_serializer_class = PaginatedCardapioSerializer
    serializer_class = ItemSerializer

    def get_queryset(self):
		order = self.request.query_params.get('order', None)
		queryset = Item.objects.all()
		if order is not None:
			if order == "desc":
				queryset = queryset.order_by("-valor")
			else:
				queryset = queryset.order_by("valor")
		return queryset


class ItemFilterViewSet(viewsets.ModelViewSet):
	model = Item
	pagination_serializer_class = PaginatedCardapioSerializer
	serializer_class = ItemSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		order = self.request.query_params.get('order', None)
		queryset = Item.objects.filter(categoria__id=id)
		if order is not None:
			if order == "desc":
				queryset = queryset.order_by("-valor")
			else:
				queryset = queryset.order_by("valor")
		return queryset


    

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.filter(id__in=Item.objects.values("categoria_id").distinct).order_by('-nome')
    pagination_serializer_class = PaginatedCategoriaSerializer
    serializer_class = CategoriaSerializer



def Orders(request):
	title = "Pedidos das mesas"
	itens = ItemPedido.objects.filter(status = 0, pedido__mesa__estabelecimento__usuario = request.user)
	return render_to_response('admin/orders.html',locals(),context_instance=RequestContext(request))

     

   

