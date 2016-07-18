# -*- coding: utf-8 -*-
from django.db import models
from decimal import Decimal
from django.db.models import Sum
from estabelecimento.models import *


STATUS_ITEM = (
        (0,'Novo'),
        (1,'Em processo'),
        (2,u'Concluído')
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


class Categoria(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento)
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.nome)

class Ingrediente(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento)
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.nome)
        
class Item(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento)
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(decimal_places = 2, max_digits = 10)
    ingredientes = models.ManyToManyField(Ingrediente)
    tempo = models.IntegerField(help_text="em horas")
    imagem = models.ImageField(upload_to= retira_acento_upload, null=True, blank=True) 
    categoria = models.ForeignKey(Categoria)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item' 
        verbose_name_plural = 'Itens'

    def __unicode__(self):
        return '{0}'.format(self.nome)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido)
    item = models.ForeignKey(Item)
    quantidade = models.IntegerField()
    status = models.IntegerField(choices=STATUS_ITEM, default=0)

    created_at = models.DateTimeField(u'Data de Criação', auto_now_add = True)
    updated_at = models.DateTimeField(u'Data de Atualização',auto_now = True)

    
    class Meta:
        verbose_name = 'Item do pedido' 
        verbose_name_plural = 'Itens dos pedidos'

    def __unicode__(self):
        return "%s"%(self.pedido)

