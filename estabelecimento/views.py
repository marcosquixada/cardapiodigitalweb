from rest_framework import permissions, viewsets, generics	
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_406_NOT_ACCEPTABLE
from rest_framework.decorators import api_view
from estabelecimento.models import Estabelecimento, Mesa, Pedido, AlertaMesa
from menu.models import Item, ItemPedido
from estabelecimento.serializers import PaginatedEstabelecimentoSerializer,EstabelecimentoSerializer, PedidoSerializer, ItemPedidoSerializer
from django.shortcuts import render_to_response
from django.template import RequestContext,Context

@api_view(['POST','GET'])
def CreateOrder(request, pk):
	try:
		mesa = Mesa.objects.get(pk=pk)
	except Mesa.DoesNotExist:
		return Response(status=HTTP_404_NOT_FOUND)

	if not Pedido.objects.filter(mesa = mesa, status= 0).exists():
		pedido = Pedido.objects.create(mesa = mesa)
		serializer = PedidoSerializer(pedido)
		return Response(serializer.data)
	else:
		return Response(status=HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST','GET','PUT'])
def Order(request, pk):
	try:
		pedido = Pedido.objects.get(pk=pk)
	except Pedido.DoesNotExist:
		return Response(status=HTTP_404_NOT_FOUND)
	if request.method == 'PUT':
		serializer = PedidoSerializer(pedido, data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		serializer = PedidoSerializer(pedido)
		return Response(serializer.data)


@api_view(['POST','GET','PUT'])
def ItemOrder(request, order_pk, item_pk):
	try:
		pedido = Pedido.objects.get(pk=order_pk)
	except Pedido.DoesNotExist:
		return Response(status=HTTP_404_NOT_FOUND)
	try:
		item = Item.objects.get(pk=item_pk)
	except Pedido.DoesNotExist:
		return Response(status=HTTP_404_NOT_FOUND)
	try:
		item_pedido = ItemPedido.objects.get(item=item, pedido=pedido)
	except ItemPedido.DoesNotExist:
		item_pedido = ItemPedido.objects.create(pedido=pedido, item=item, quantidade=0)

	if request.method == 'PUT':
		serializer = ItemPedidoSerializer(item_pedido, data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		if item_pedido.status != 0:
			item_pedido.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(status=HTTP_406_NOT_ACCEPTABLE)
	else:
		serializer = ItemPedidoSerializer(item_pedido)
		return Response(serializer.data)


def QrCode(request):
	title = "QrCode das Mesas do Estabelecimento"
	mesas = Mesa.objects.filter(estabelecimento__usuario = request.user)
	return render_to_response('admin/qrcodes.html',locals(),context_instance=RequestContext(request))


def Alertas(request):
	title = "Alertas das mesas"
	alertas = AlertaMesa.objects.filter(atendido = False)
	return render_to_response('admin/alertas.html',locals(),context_instance=RequestContext(request))


class EstabelecimentoViewSet(viewsets.ModelViewSet):
	model = Estabelecimento
	pagination_serializer_class = PaginatedEstabelecimentoSerializer
	serializer_class = EstabelecimentoSerializer

	def get_queryset(self):
		queryset = Item.objects.all()
		return queryset

     

   

