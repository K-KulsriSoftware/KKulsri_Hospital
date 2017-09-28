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
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^doctor-detail/(?P<doctor_name>\w{0,50})-(?P<doctor_surname>\w{0,50})/$', app.views.doctor_detail, name='doctor_detail '),
    url(r'^register', app.views.register, name='register '),
    url(r'^member', app.views.member, name='member '),
    url(r'^departments', app.views.departments, name='departments '),
    url(r'^regular-packages', app.views.regular_packages, name='regular_packages '),
    url(r'^special-packages', app.views.special_packages, name='special_packages '),
    url(r'^doctor-search', app.views.search_for_doctor, name='search_for_doctor '),
    url(r'^doctor$', app.views.doctor, name='doctor '),
    url(r'^confirm', app.views.confirm, name='confirm '),
    url(r'^payment', app.views.payment, name='payment '),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
