from django.contrib import admin
from menu.models import *
from easy_select2 import select2_modelform

class ItemAdmin(admin.ModelAdmin):
	fieldsets = [('Dados',{'classes': ('grp-collapse grp-open',),
                              'fields': [('nome','valor'),
                                    	('ingredientes'),
                              			('categoria','tempo'),
                              			],}),]
	
	list_display = ['nome','categoria','valor','tempo']
	list_filter = ['categoria','ingredientes']
	search_fields = ['nome','categoria__nome']

	form = select2_modelform(Item, attrs={'width': '250px'})

	def get_queryset(self, request):
		qs = super(ItemAdmin, self).get_queryset(request)
		if request.user.is_superuser:
		  return qs
		return qs.filter(estabelecimento__usuario=request.user)

	def save_model(self, request, obj, form, change):
		if obj.id is None:
			obj.estabelecimento = Estabelecimento.objects.get(usuario = request.user)
		obj.save()


class ItemPedidoAdmin(admin.ModelAdmin):
	fieldsets = [('Dados',{'classes': ('grp-collapse grp-open',),
                              'fields': [('pedido','item'),
                                    	('quantidade'),
                              			('status'),
                              			],}),]
	
	list_display = ['pedido','item','quantidade','status']
	list_filter = ['pedido__mesa','item']

	form = select2_modelform(ItemPedido, attrs={'width': '250px'})

	def get_queryset(self, request):
		qs = super(ItemPedidoAdmin, self).get_queryset(request)
		if request.user.is_superuser:
		  return qs
		return qs.filter(pedido__mesa__estabelecimento__usuario=request.user)


class IngredienteAdmin(admin.ModelAdmin):
	fieldsets = [('Dados',{'classes': ('grp-collapse grp-open',),
                              'fields': [('nome')
                              			],}),]
	
	list_display = ['nome']
	search_fields = ['nome']

	def get_queryset(self, request):
		qs = super(IngredienteAdmin, self).get_queryset(request)
		if request.user.is_superuser:
		  return qs
		return qs.filter(estabelecimento__usuario=request.user)

	def save_model(self, request, obj, form, change):
		if obj.id is None:
			obj.estabelecimento = Estabelecimento.objects.get(usuario = request.user)
		obj.save()


class CategoriaAdmin(admin.ModelAdmin):
	fieldsets = [('Dados',{'classes': ('grp-collapse grp-open',),
                              'fields': [('nome')
                              			],}),]
	
	list_display = ['nome']
	search_fields = ['nome']
	
	def get_queryset(self, request):
		qs = super(CategoriaAdmin, self).get_queryset(request)
		if request.user.is_superuser:
		  return qs
		return qs.filter(estabelecimento__usuario=request.user)

	def save_model(self, request, obj, form, change):
		if obj.id is None:
			obj.estabelecimento = Estabelecimento.objects.get(usuario = request.user)
		obj.save()


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)


