from django.conf.urls import include, patterns, url

from rest_framework_nested import routers
from django.conf import settings
from menu.views import ItemViewSet, ItemFilterViewSet, CategoriesViewSet, Orders
from estabelecimento.views import EstabelecimentoViewSet, CreateOrder,ItemOrder, \
Order,QrCode, Alertas, AlertaOrder
from jaPedi.views import IndexView
from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'items/categories', CategoriesViewSet)
router.register(r'items/(?P<id>[0-9]+)', ItemFilterViewSet)
router.register(r'items', ItemViewSet)
router.register(r'estabelecimentos', EstabelecimentoViewSet)


urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^qr_codes/', QrCode),
    url(r'^alertas/', Alertas, name="alertas"),
    url(r'^orders/', Orders, name="orders"),
    url(r'create_order/(?P<pk>[0-9]+)$',CreateOrder),
    url(r'alerta_order/(?P<order_pk>[0-9]+)$',AlertaOrder),
	url(r'order/(?P<pk>[0-9]+)$',Order),
	url(r'item_order/(?P<order_pk>[0-9]+)/(?P<item_pk>[0-9]+)$',ItemOrder),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'', include('django_autocomplete.urls')),
    url(r'^.*$', IndexView.as_view(), name='index'),
)
