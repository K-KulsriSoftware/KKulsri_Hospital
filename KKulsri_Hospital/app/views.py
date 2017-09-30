"""
Definition of views.
"""
# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import redirect, render
from django.http import HttpRequest, JsonResponse
from django.template import RequestContext
from datetime import datetime
from .API.API import API
from pymongo import MongoClient
import base64


api = API()

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

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


def doctor_detail(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    status, result = api.show_detail(request.GET.get('doctor_name'), request.GET.get('doctor_surname'))
    if status:
        return render(
            request,
            'app/doctor-detail.html',
            {
                'doctor': result
            }
        )
    else:
        raise Http404("No doctor found")


def register(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        username = request.POST['username']
        patient_name_title = request.POST['patient_name_title']
        patient_name = request.POST['patient_name']
        patient_surname = request.POST['patient_surname']
        patient_img = request.POST['patient_img']
        id_card_number = request.POST['id_card_number']
        gender = request.POST['gender']
        order_ids = request.POST['order_ids']
        birthday_year = request.POST['birthday_year']
        birthday_month = request.POST['birthday_month']
        birthday_day = request.POST['birthday_day']
        blood_group_abo = request.POST['blood_group_abo']
        blood_group_rh = request.POST['blood_group_rh']
        race = request.POST['race']
        nationallity = request.POST['nationallity']
        Religion = request.POST['Religion']
        Status = request.POST['Status']
        pateint_address = request.POST['pateint_address']
        occupy = request.POST['occupy']
        telphone_number = request.POST['telphone_number']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        emergency_name = request.POST['emergency_name']
        emergency_phone = request.POST['emergency_phone']
        emergency_addr = request.POST['emergency_addr']
        email = request.POST['email']
        congenital_disease = request.POST['congenital_disease']
        submit = request.POST['submit']
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

def doctor_search_api(request):
    status, result = api.find_doctors(request.GET.get('package_id'), request.GET.get('days').split(','), request.GET.get('time'), request.GET.get('doctor_firstname'), request.GET.get('doctor_lastname'), request.GET.get('gender'))
    return JsonResponse(result)

def doctor(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    status, result = api.show_doctor_in_department()
    return render(
        request,
        'app/doctor.html',
        {
            'departments': result
        }
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

def admin_mongo(request):
    assert isinstance(request, HttpRequest)
    status, result = api.get_all_collections_name()
    result.sort()
    return render(
        request,
        'app/admin-mongo.html',
        {
            'header_title': 'mongoDB Admin',
            'collections': result,
            'DATABASE': True,
            'logo_link': '/admin-mongo'
        }
    )

def admin_mongo_collection(request, collection_name):
    assert isinstance(request, HttpRequest)
    status, result = {
        'buildings': api.get_all_buildings_name(),
        'departments': api.get_all_departments_name(),
        'doctors': api.get_all_doctors_name(),
        'orders': api.get_all_orders(),
        'patients': api.get_all_patients_name(),
        'users': api.get_all_users_name(),
        'packages': api.get_all_packages_name()
    }.get(collection_name)
    return render(
        request,
        'app/admin-mongo.html',
        {
            'header_title': 'mongoDB Admin',
            'collection_name': collection_name,
            'data': result,
            'COLLECTION': True,
            'toolbar': True,
            'logo_link': '/admin-mongo'
        }
    )
