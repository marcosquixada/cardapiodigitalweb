from rest_framework import permissions, viewsets, generics	
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_406_NOT_ACCEPTABLE
from rest_framework.decorators import api_view
from estabelecimento.models import Estabelecimento, Mesa, Pedido, AlertaMesa
from menu.models import Item, ItemPedido
from estabelecimento.serializers import PaginatedEstabelecimentoSerializer,EstabelecimentoSerializer, PedidoSerializer, PedidoSmallSerializer, ItemPedidoSerializer
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
		print pedido
		serializer = PedidoSerializer(pedido)
		print serializer.data
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
		serializer = PedidoSmallSerializer(pedido, data=request.data)
		if serializer.is_valid():	
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
	else:
		serializer = PedidoSerializer(pedido)
		return Response(serializer.data)


@api_view(['POST','GET'])
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

	if request.method == 'POST':
		item_pedido.quantidade = int(item_pedido.quantidade) + int(request.POST.get("quantidade"))
		item_pedido.save()
		serializer = ItemPedidoSerializer(item_pedido)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ItemPedidoFullSerializer(item_pedido, data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		item_pedido.delete()
		return Response(status=HTTP_204_NO_CONTENT)

@api_view(['GET'])
def AlertaOrder(request, order_pk):
	try:
		pedido = Pedido.objects.get(pk=order_pk)
	except Pedido.DoesNotExist:
		return Response(status=HTTP_404_NOT_FOUND)

	try:
		AlertaMesa(mesa = pedido.mesa, atendido = False).save()
		return Response(status=HTTP_201_CREATED)
	except:
		return Response(status=HTTP_400_BAD_REQUEST)

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

     

   

