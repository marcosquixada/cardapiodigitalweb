from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<report_id>\d+)/$', 'report.views.report', name="report"),
)