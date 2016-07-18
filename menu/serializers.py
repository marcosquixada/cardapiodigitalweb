from rest_framework import serializers, pagination
from menu.models import Item, Categoria, Ingrediente



class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        depth = 2

        fields = ('id', 'nome')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(CategoriaSerializer, self).get_validation_exclusions()

        return exclusions

class IngredienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingrediente
        depth = 2

        fields = ('id', 'nome')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ItemSerializer, self).get_validation_exclusions()

        return exclusions


class ItemSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True, required=False)
    ingredientes = IngredienteSerializer(many=True, required=False)

    class Meta:
        model = Item
        depth = 2
        
        fields = ('id', 'nome', 'valor', 'categoria' ,'ingredientes', 'tempo','imagem','created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ItemSerializer, self).get_validation_exclusions()

        return exclusions


class PaginatedCardapioSerializer(pagination.PaginationSerializer):
    
    class Meta:
        object_serializer_class = ItemSerializer


class PaginatedCategoriaSerializer(pagination.PaginationSerializer):
    
    class Meta:
        object_serializer_class = CategoriaSerializer
