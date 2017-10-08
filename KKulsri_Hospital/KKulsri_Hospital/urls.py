"""
Definition of urls for KKulsri_Hospital.
"""
# -*- coding: utf-8 -*-

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^doctor-detail/', app.views.doctor_detail, name='doctor_detail '),
    url(r'^member/$', app.views.member, name='member '),
    url(r'^member/edit/$', app.views.edit_member_info, name='member '),
    url(r'^departments/', app.views.departments, name='departments '),
    url(r'^regular-packages/', app.views.regular_packages, name='regular_packages '),
    url(r'^special-packages/(?P<package_id>\w{0,50})/$', app.views.special_packages, name='special_packages '),
    url(r'^doctor-search/', app.views.search_for_doctor, name='search_for_doctor '),
    url(r'^doctor/$', app.views.doctor, name='doctor '),
    url(r'^confirm/', app.views.confirm, name='confirm '),
    url(r'^payment/', app.views.payment, name='payment '),
    url(r'^admin-mongo/$', app.views.admin_mongo, name='admin-mongo '),
    url(r'^admin-mongo/collection/(?P<collection_name>\w{0,50})/$', app.views.admin_mongo_collection, name='admin-mongo-collection'),
    url(r'^doctor_search_api/', app.views.doctor_search_api, name='doctor_search_api'),
    url(r'^doctor_auto_search_api/', app.views.doctor_auto_search_api, name='doctor_auto_search_api'),
    url(r'^login/$', app.views.login,name='login'),
    url(r'^logout$', app.views.logout),
    url(r'^register/', app.views.register, name='register'),
    url(r'^signup/', app.views.signup, name='signup'),
    url(r'^account_activation_sent/',
        app.views.account_activation_sent, name='account_activation_sent'),
    url(r'^account_activation_invalid/',
        app.views.account_activation_invalid, name='account_activation_invalid'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',app.views.activate, name='activate'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
