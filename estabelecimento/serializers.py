from rest_framework import serializers, pagination
from estabelecimento.models import Estabelecimento, Pedido, FormaPagamento
from menu.models import ItemPedido



class EstabelecimentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estabelecimento

        fields = ('id', 'nome')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(EstabelecimentoSerializer, self).get_validation_exclusions()

        return exclusions


class FormaPagamentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FormaPagamento

        fields = ('id', 'forma','logo')
        read_only_fields = ('id',)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(FormaPagamentoSerializer, self).get_validation_exclusions()

        return exclusions


class PedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pedido

        fields = ('id', 'mesa','forma_pagamento','status','itens','total','formas_pagamento')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PedidoSerializer, self).get_validation_exclusions()

        return exclusions


class ItemPedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItemPedido

        fields = ('id', 'pedido','item','quantidade')
        read_only_fields = ('id',)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ItemPedidoSerializer, self).get_validation_exclusions()

        return exclusions

class PaginatedEstabelecimentoSerializer(pagination.PaginationSerializer):
    
    class Meta:
        object_serializer_class = EstabelecimentoSerializer
