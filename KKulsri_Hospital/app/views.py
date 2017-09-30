"""
Definition of views.
"""
# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .API.API import API
from pymongo import MongoClient
import base64


api = API()

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    # return render(
    #     request,
    #     'app/index.html',
    #     {
    #         'title':'Home Page',
    #         'year':datetime.now().year,
    #     }
    # )
    return redirect('/departments')

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def doctor_detail(request, doctor_name, doctor_surname):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    doctor_name = base64.b64decode(doctor_name.encode('utf8')).decode('utf8')
    doctor_surname = base64.b64decode(doctor_surname.encode('utf8')).decode('utf8')
    status, result = api.show_detail(doctor_name, doctor_surname)
    return render(
        request,
        'app/doctor-detail.html',
        {
            'doctor': result
        }
    )


def register(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':

        username = request.POST['username']
        # เติมให้ครบ

        status, result = api.register(username, patient_name_title, patient_name, patient_surname, patient_img,
            id_card_number, gender, order_ids, birthday_year, birthday_month, birthday_day,
            blood_group_abo, blood_group_rh, race, nationallity, Religion, Status, 
            pateint_address, occupy, telphone_number, father_name, mother_name, emergency_name,
            emergency_phone, emergency_addr, email, congenital_disease, submit)
        if status:
            return redirect('/')
        else:
            return render(
                request,
                'app/register.html',
            )
    else:
        return render(
            request,
            'app/register.html',
        )

def member(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/member.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )


def departments(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    status, result = api.show_departments()
    return render(
        request,
        'app/departments.html',
        {
            'departments': result
        }
    )


def regular_packages(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    status, result = api.show_general_list()
    return render(
        request,
        'app/regular-package.html',
        {
            'packages': result
        }
    )


def special_packages(request, package_id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    status, result = api.show_special_package_info(package_id)
    return render(
        request,
        'app/special_packages.html',
        {
            'package': result
        }
    )


def search_for_doctor(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/doctor-search.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )

def doctor(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/doctor.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )


def confirm(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/confirm.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )


def payment(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payment.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )
