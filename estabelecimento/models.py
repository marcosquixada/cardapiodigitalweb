# -*- coding: utf-8 -*-
from django.db import models
from decimal import Decimal
from django.db.models import Sum
from django.contrib.auth.models import User


STATUS_PEDIDO = (
        (0,'Aberto'),
        (1,'Fechado')
    )


def retira_acento_upload(a,b):
        import re
        import unicodedata
        import inspect
        from datetime import datetime
        
        l =  locals()
        path = "%s/%s" % (unicodedata.normalize('NFKD', unicode(l['a'].__class__._meta.verbose_name_plural.lower())).encode('ascii', 'ignore'), datetime.now().year)
    
        ext = b.split('.')[-1] #pega ultima ocorrência do split
        url = unicodedata.normalize('NFKD', b).encode('ascii', 'ignore')
        url = re.sub(r'[^\w\d-]', '', url.replace(' ', '-').replace('--', '').lower())
        return 'arquivos/%s/%s' % (path, url[:-4]+'.'+ext)

class Estabelecimento(models.Model):

    usuario = models.ForeignKey(User)

    nome = models.CharField('Nome do estabelecimento', max_length = 100)
    cnpj = models.CharField(max_length = 20)


    rua = models.CharField('Logradouro',max_length = 100,null=True, blank=True)
    complemento = models.CharField(max_length = 30, null=True, blank=True)
    numero = models.CharField(max_length=40, null=True, blank=True)
    bairro = models.CharField(max_length = 100, null=True, blank=True)
    municipio = models.CharField(max_length = 100, null=True, blank=True)
    estado = models.CharField(max_length = 3, null=True, blank=True)
    cep = models.CharField(max_length = 9, null=True, blank=True)

    class Meta:
        verbose_name = 'Estabelecimento' 
        verbose_name_plural = 'Estabelecimentos'

    def __unicode__(self):
        return "%s"%(self.nome)

class Mesa(models.Model):

    estabelecimento = models.ForeignKey(Estabelecimento)
    mesa = models.CharField(max_length=100)

    position = models.PositiveSmallIntegerField("Position", null=True)


    class Meta:
        verbose_name = 'Mesa' 
        verbose_name_plural = 'Mesas'
        ordering = ('position', )

    def qrcode(self):
        return "http://10.1.27.84:8000/create_order/%s"%(self.id)

    def __unicode__(self):
        return "%s"%(self.mesa)


class AlertaMesa(models.Model):
    mesa = models.ForeignKey(Mesa)
    atendido = models.BooleanField()
    created_at = models.DateTimeField(u'Data de Criação', auto_now_add = True)
    updated_at = models.DateTimeField(u'Data de Atualização',auto_now = True)


    class Meta:
        verbose_name = 'Alerta da Mesa' 
        verbose_name_plural = 'Alertas das Mesas'


class FormaPagamento(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento)
    forma = models.CharField(max_length=100)
    logo = models.ImageField(upload_to= retira_acento_upload) 

    position = models.PositiveSmallIntegerField("Position", null=True)

    class Meta:
        verbose_name = 'Forma de pagamento' 
        verbose_name_plural = 'Formas de pagamento'

    def __unicode__(self):
        return "%s"%(self.forma)

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa)
    status = models.IntegerField(choices=STATUS_PEDIDO, default=0)
    forma_pagamento = models.ForeignKey(FormaPagamento, null=True, blank=True)
    created_at = models.DateTimeField(u'Data de Criação', auto_now_add = True)
    updated_at = models.DateTimeField(u'Data de Atualização',auto_now = True)

    def itens(self):
        from menu.models import ItemPedido

        itens = ItemPedido.objects.filter(pedido = self).values_list('item__nome')
        return itens

    def total(self):
        from menu.models import ItemPedido
        total = 0.0
        itens = ItemPedido.objects.filter(pedido = self)
        for item in itens:
            total = total + float(item.item.valor * item.quantidade)
        return total

    def categorias(self):
        from menu.serializers import CategoriaSerializer
        from menu.models import Categoria
        categorias = Categoria.objects.filter(estabelecimento = self.mesa.estabelecimento)
        serializer = CategoriaSerializer(categorias, many=True)
        return serializer.data

    def formas_pagamento(self):
        from serializers import FormaPagamentoSerializer
        forma_pagamento = FormaPagamento.objects.filter(estabelecimento = self.mesa.estabelecimento)
        serializer = FormaPagamentoSerializer(forma_pagamento, many=True)
        return serializer.data

    class Meta:
        verbose_name = 'Pedido' 
        verbose_name_plural = 'Pedidos'

    def __unicode__(self):
        return "%s"%(self.mesa)

