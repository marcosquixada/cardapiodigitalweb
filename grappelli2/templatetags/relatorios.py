from django import template
from report.models import ReportType
from django.db.models import Q

register = template.Library()

def get_relatorios(request):
    relatorios = []
    if request.user.is_superuser:
        reports = ReportType.objects.all()
    else:
        reports = ReportType.objects.filter(Q(permissao__contains=request.user.groups.all()) | Q(permissao__isnull=True))
    for report in reports:
        relatorios.append("<li><a href='%s'>%s</a></li>" %(report.get_absolute_url(),report.titulo))
    return {
        'relatorios': relatorios
    }

def get_relatorios_menu(request):
    relatorios = []
    if request.user.is_superuser:
        reports = ReportType.objects.all()
    else:
        reports = ReportType.objects.filter(Q(permissao__contains=request.user.groups.all()) | Q(permissao__isnull=True))
    for report in reports:
        relatorios.append("<a href='%s'><strong>%s</strong></a>" %(report.get_absolute_url(),report.titulo))
    return {
        'relatorios': relatorios
    }

register.inclusion_tag('admin/relatorios.html')(get_relatorios)
register.inclusion_tag('admin/relatorios_menu.html')(get_relatorios_menu)