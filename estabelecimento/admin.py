# -*- coding: utf-8 -*-
from django.contrib import admin
from estabelecimento.models import *
from menu.models import *
from django_autocomplete.widgets import AutocompleteCTWidget
from django_admin_bootstrapped.admin.models import SortableInline
from easy_select2 import select2_modelform
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from daterange_filter.filter import DateRangeFilter

class MesaInline(SuperInlineModelAdmin, admin.TabularInline, SortableInline):
    model = Mesa
    exclude = ('position',)
    sortable_field_name = 'position'
    extra = 1


class FormaPagamentoInline(SuperInlineModelAdmin, admin.TabularInline, SortableInline):
    model = FormaPagamento
    exclude = ('position',)
    sortable_field_name = 'position'
    extra = 1

class ItemPedidoInline(SuperInlineModelAdmin, admin.TabularInline, SortableInline):
    model = ItemPedido
    form = select2_modelform(ItemPedido, attrs={'width': '250px'})
    exclude = ('position',)
    sortable_field_name = 'position'
    extra = 1
    

class EstabelecimentoAdmin(SuperModelAdmin):
  fieldsets = [('Dados Gerais',{'classes': ('grp-collapse grp-open',),
                              'fields': [('nome','usuario')
                                    ],}),
  (u'Endereço',{'classes': ('grp-collapse grp-open',),
                     'fields': [('rua','complemento'),
                                    ('bairro','numero'),
                                    ('cep'),
                                    ('municipio','estado')],}),]
  list_display = ['nome','usuario']
  list_filter = ['usuario']
  search_fields = ['nome']

  form = select2_modelform(Estabelecimento, attrs={'width': '250px'})

  inlines = [MesaInline, FormaPagamentoInline]

  def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('usuario',)
        return self.readonly_fields

  def get_form(self, request, obj=None, **kwargs):
    current_user = request.user
    if request.user.is_superuser:
        self.exclude = ('usuario',)
    form = super(EstabelecimentoAdmin, self).get_form(request, obj, **kwargs)
    return form




class AlertaMesaAdmin(admin.ModelAdmin):
  fieldsets = [('Dados Gerais',{'classes': ('grp-collapse grp-open',),
                              'fields': [('mesa'),
                                          ('atendido')
                                    ],}),]
  list_display = ['mesa','atendido','created_at','updated_at']
  list_filter = ['created_at', 'atendido','mesa__mesa','mesa__estabelecimento__nome']

  form = select2_modelform(AlertaMesa, attrs={'width': '250px'})

  def get_queryset(self, request):
    qs = super(AlertaMesaAdmin, self).get_queryset(request)
    if request.user.is_superuser:
      return qs
    return qs.filter(mesa__estabelecimento__usuario=request.user)

class PedidoAdmin(admin.ModelAdmin):
  fieldsets = [('Dados Gerais',{'classes': ('grp-collapse grp-open',),
                              'fields': [('mesa'),
                                          ('status'),
                                          ('forma_pagamento')
                                    ],}),]
  list_display = ['mesa','itens','status','forma_pagamento','created_at','updated_at']
  list_filter = ['created_at','mesa__mesa','mesa__estabelecimento__nome']
  form = select2_modelform(Pedido, attrs={'width': '250px'})

  inlines = [ItemPedidoInline]
  def get_queryset(self, request):
    qs = super(PedidoAdmin, self).get_queryset(request)
    if request.user.is_superuser:
      return qs
    return qs.filter(mesa__estabelecimento__usuario=request.user)


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(AlertaMesa, AlertaMesaAdmin)
