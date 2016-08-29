from rest_framework import serializers, pagination
from estabelecimento.models import Estabelecimento, Pedido, FormaPagamento, Mesa
from menu.serializers import ItemSerializer
from menu.models import ItemPedido



class EstabelecimentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estabelecimento

        fields = ('id', 'nome')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(EstabelecimentoSerializer, self).get_validation_exclusions()

        return exclusions


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        exclude = ('position','estabelecimento')


class FormaPagamentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FormaPagamento

        fields = ('id', 'forma','logo')
        read_only_fields = ('id',)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(FormaPagamentoSerializer, self).get_validation_exclusions()

        return exclusions


class ItemPedidoSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ItemPedido
        depth = 2

        fields = ('id', 'pedido','item','quantidade','created_at')
        read_only_fields = ('id',)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ItemPedidoSerializer, self).get_validation_exclusions()

        return exclusions


class ItemPedidoShortSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItemPedido
        depth = 2

        fields = ('id', 'item','quantidade','created_at')
        read_only_fields = ('id',)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ItemPedidoSerializer, self).get_validation_exclusions()

        return exclusions

class PedidoSerializer(serializers.ModelSerializer):
    mesa = MesaSerializer()
    itens = ItemPedidoShortSerializer(many=True, required=False)

    class Meta:
        model = Pedido
        depth = 2

        fields = ('id', 'mesa', 'status','itens','total','formas_pagamento','categorias')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PedidoSerializer, self).get_validation_exclusions()

        return exclusions

class PedidoSmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        depth = 2

        fields = ('id','status','forma_pagamento')
        read_only_fields = ('id',)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PedidoSmallSerializer, self).get_validation_exclusions()

        return exclusions

class PaginatedEstabelecimentoSerializer(pagination.PaginationSerializer):
    
    class Meta:
        object_serializer_class = EstabelecimentoSerializer
