# -*- coding: utf-8 -*-
from django.utils.encoding import smart_str
from datetime import date, datetime
from django.conf import settings
from configuracao.models import *

def capitalize(string):
    return string[0].upper()+string[1:]

def many_to_many_display(list):
    display = ""
    for i, item in enumerate(list):
        display += smart_str(item)
        if i != len(list)-1: display += ", "
    return display

def get_display(queryset, report):
    try:
        model = queryset.model
    except:
        model = queryset
    if "__" in report:
        value = getattr(model, report.split("__")[0])
        return get_display(value, report.replace(report.split("__")[0]+"__", ""))
    else:
        try:
            value = smart_str(capitalize(model._meta.get_field(report).verbose_name))
        except:
           value = smart_str(capitalize(report))
        return value.replace("_", " ")


def get_value(query, report):
    if "__" in report:
        value = getattr(query, report.split("__")[0])
        return get_value(value, report.replace(report.split("__")[0]+"__", ""))
    else:
        value = getattr(query, report)
        if value is None or value == "":
            value = " - "
        elif type(value) is date:
            if value is not None:
                value = value.strftime("%d/%m/%Y")
            else:
                value = " - "
        elif type(value) is datetime:
            if value is not None:
                value = value.strftime("%d/%m/%Y")
            else:
                value = " - "
        elif type(value) is bool:
            if value:
                value = "Sim"
            else:
                value = "Não"
        elif type(value) is unicode and value != " - " and len(value) <= 3:
            try:
                func = getattr(query, "get_"+report+"_display")
                value = func()
            except:
                pass
        elif "instancemethod" in str(type(value)):
            func = getattr(query, report)
            value = func()
        elif "django.db.models.fields.related.ManyRelatedManager" in str(type(value)):
            value = many_to_many_display(value.all())
        return smart_str(value)


def html_report_pendencias(report_header, list_report, queryset):
    parceiros = ""
    parc = []
    for i,query in enumerate(queryset):
        if get_value(query, "parceiro") not in parc:
            parceiros = parceiros + get_value(query, "parceiro") + "," 
            parc.append(get_value(query, "parceiro"))
    parceiros = parceiros[:len(parceiros)-1]
    parceiros = parceiros.replace(" - ","")
    html = """
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            @page {size: a4 landscape; margin: 1cm; }
            table {font: 88%/1.7em "Trebuchet MS", "Bitstream Vera Sans", Verdana, Helvetica, sans-serif;
            border-collapse: separate; border-spacing: 0; margin: 0 0 1em 0; color:#000;}
            a {color: #09f; text-decoration: none; border-bottom: 1px solid;}
            a:visited {color: #c3c; font-weight: normal;}
            a:hover {border-bottom-style: dotted;}
            thead th,
            thead td {font-weight: bold; line-height:normal; text-align: left; border-bottom: 0.4em solid #D9D919;}
            tfoot th,
            tfoot td {text-align: left; border-top: 0.4em solid #09f; font-weight: bold}
            th,
            td {padding: 0.25em;}
            tbody th,
            td {text-align: left; vertical-align: top;}
            tbody th {font-weight: normal; white-space: nowrap;}
            tbody th a:link,
            tbody th a:visited {font-weight: bold;}
            tbody th + td {white-space: nowrap;}
            tbody td,
            tbody th {border: 1px solid #fff; border-width: 1px 0;}
            tbody tr.odd th,
            tbody tr.odd td {border-color: #deded8; background: #f9f9fb;}
            tbody tr:hover td,
            tbody tr:hover th {background: #fbfbf8;}
            caption {font-weight: bold; font-size: 1.7em; text-align: left; margin: 0; padding: 0.5em 0.25em;}
            td + td + td + td {white-space: nowrap;}
        </style>
        <table >
          <tr>
            <td align="left" width="35%"><img src='http://lealmoreira.planegis.com.br/static/admin/img/logo-lealmoreira.png' width="150px"/></td>
            <td align="left" valign="middle" style="font-size:22px">"""+smart_str(report_header)+"""</td>
          </tr>
          <tr>
              <td>Responsável:"""+ parceiros +""" </td>
          </tr>
        </table> """

    html += """
        <table >
              <thead>
              <tr>
                <th width="3%" scope="col" >Nº</th>"""
    for report in list_report:
        value = get_display(queryset, report)
        if value == "Cliente":
            html += """<th width="25%" scope='col'>""" + value + """</th>""" 
        elif value == "Prazo" or value == "Processo":
            html += """<th width="5%" scope='col'>""" + value + """</th>""" 
        elif value == "Parceiro" or value == "Beneficio":
            html += """<th width="10%" scope='col'>""" + value + """</th>""" 
        else:
            html += "<th scope='col'>%s</th>" % (value)

    html += "</tr></thead><tbody>"

    for i,query in enumerate(queryset):
        if i%2==0: z=2
        else: z=3
        if z == 3:
            html += "<tr>"
        else:
            html += "<tr class='odd'>"
        html += "<td >%s</td>" %(i+1)
        for report in list_report:
            value = get_value(query, report)
            html += "<td >%s</td>" % (value)
        html += "</tr></tbody>"

    html += "</table>"
    return html

def html_report_generic(report_header, list_report, queryset):
    html = """
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            @page {size: a4 landscape; margin: 1cm; }
            table {font: 88%/1.7em "Trebuchet MS", "Bitstream Vera Sans", Verdana, Helvetica, sans-serif;
            border-collapse: separate; border-spacing: 0; margin: 0 0 1em 0; color:#000;}
            a {color: #09f; text-decoration: none; border-bottom: 1px solid;}
            a:visited {color: #c3c; font-weight: normal;}
            a:hover {border-bottom-style: dotted;}
            thead th,
            thead td {font-weight: bold; line-height:normal; text-align: left; border-bottom: 0.4em solid #09f;}
            tfoot th,
            tfoot td {text-align: left; border-top: 0.4em solid #09f; font-weight: bold}
            th,
            td {padding: 0.25em;}
            tbody th,
            td {text-align: left; vertical-align: top;}
            tbody th {font-weight: normal; white-space: nowrap;}
            tbody th a:link,
            tbody th a:visited {font-weight: bold;}
            tbody th + td {white-space: nowrap;}
            tbody td,
            tbody th {border: 1px solid #fff; border-width: 1px 0;}
            tbody tr.odd th,
            tbody tr.odd td {border-color: #deded8; background: #f9f9fb;}
            tbody tr:hover td,
            tbody tr:hover th {background: #fbfbf8;}
            caption {font-weight: bold; font-size: 1.7em; text-align: left; margin: 0; padding: 0.5em 0.25em;}
            td + td + td + td {white-space: nowrap;}
        </style>
        <table >
          <tr>
            <td align="center" class="head" ><h1>"""+smart_str(report_header)+"""</td>
          </tr>
        </table> """

    html += """
        <table >
              <thead>
              <tr>
                <th width="3%" scope="col" >Nº</th>"""
    percent =  97/len(list_report)
    for report in list_report:
        value = get_display(queryset, report)
        html += '<th scope="col" width="%s">%s</th>'% (str(int(percent))+"%",value)

    html += "</tr></thead><tbody>"
    
    for i,query in enumerate(queryset):
        if i%2==0: z=2
        else: z=3
        if z == 3:
            html += "<tr>"
        else:
            html += "<tr class='odd'>"
        html += '<td width="%s">%s</td>' %("3%",i+1)
        for report in list_report:
            value = get_value(query, report)
            html += "<td width='%s'>%s</td>" % (str(int(percent))+"%", value)
        html += "</tr></tbody>"

    html += "</table>"
    return html



def html_report_generic_detailed(report_header, fieldsets_report, query):

    html = """
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            body { font-family:Helvetica Narrow, sans-serif; font-size:12px; }
            .desc {font-weight: bolder; border-bottom: 2px #000 solid; font-weight:bolder; padding: 10px 0 0 0;}
            .pad3 {padding: 3px; color: #666;}
            .bottom{ border-bottom: 2px #000 solid;}
            .head {padding-bottom: 10px;}
        </style>
        <img  style="float:left" src='http://lealmoreira.planegis.com.br/static/admin/img/logo-lealmoreira_azul.png'  width="150px"/>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td align="center" class="head">"""+smart_str(report_header)+"""</td>
          </tr>
        </table> """

    html += """
        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">"""
    for fieldset in fieldsets_report:
        html += """
            <tr>
                <td colspan="2" class="desc">"""+smart_str(fieldset[0])+"""</td>
            </tr>
        """

        for key,field in enumerate(fieldset[1]['fields']):
            if key%2 == 0: html += "<tr>"
            html += """
                <td width="50%" class="pad3"><strong>"""+smart_str(get_display(query, field))+""": </strong>"""+smart_str(get_value(query, field))+"""</td>
            """
            if key%2 != 0: html += "</tr>"
        if len(fieldset[1]['fields'])%2 == 0:
            html += "</tr>"

    html += """<tr>
                    <td width="50%" class="bottom"></td>
                    <td width="50%" class="bottom"></td>
                </tr>
            </table>"""

    return html