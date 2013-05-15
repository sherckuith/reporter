# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('reporter.core.views',
    url(r'^$',
        view='index',
        name='index'),
    url(r'^(?P<pk>\d+)/xml/$',
        view='report_xml',
        name='report_xml'),
    url(r'^(?P<pk>\d+)/$',
        view='report_html',
        name='report_html'),
    url(r'^latest/$',
        view='report_latest',
        name='report_latest'),
)
