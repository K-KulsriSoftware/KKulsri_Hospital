"""
Definition of views.
"""
# -*- coding: utf-8 -*-
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpRequest, JsonResponse
from django.template import RequestContext
from datetime import datetime
from .API.API import API
from pymongo import MongoClient
import base64
# import app.forms

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


@login_required
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
    if 'selected_package' not in request.session or 'selected_doctor' not in request.session:
        return redirect('/doctor-search')
    assert isinstance(request, HttpRequest)
    status, result = api.show_detail(request.session['selected_doctor']['doctor_name'], request.session['selected_doctor']['doctor_surname'])
    if status:
        status, package = api.show_special_package_info(request.session['selected_package'])
        return render(
            request,
            'app/doctor-detail.html',
            {
                'title': 'ข้อมูลแพทย์',
                'doctor': result,
                'selected_package': package
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
                {
                    'title': 'สมัครสมาชิก'
                }
            )
    else:
        return render(
            request,
            'app/register.html',
            {
                'title': 'สมัครสมาชิก'
            }
        )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required
def member(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/member.html',
        {
            'title': 'แก้ไขข้อมูลสมาชิก'
        }
    )


def departments(request):
    """Renders the about page."""
    if 'selected_package' in request.session:
        del request.session['selected_package']
    assert isinstance(request, HttpRequest)
    status, result = api.show_departments()
    return render(
        request,
        'app/departments.html',
        {
            'title': 'แผนกและแพ็คเกจ',
            'departments': result
        }
    )


def regular_packages(request):
    """Renders the about page."""
    if request.method == 'POST':
        request.session['selected_package'] = request.POST['package']
        return redirect('/doctor-search/')
    assert isinstance(request, HttpRequest)
    status, result = api.show_general_list()
    return render(
        request,
        'app/regular-package.html',
        {
            'title': 'ตรวจสุขภาพทั่วไป',
            'packages': result
        }
    )


def special_packages(request, package_id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    status, result = api.show_special_package_info(package_id)
    print(result)
    return render(
        request,
        'app/special_packages.html',
        {
            'title': 'รายละเอียดแพ็คเกจ',
            'package': result
        }
    )


def search_for_doctor(request):
    """Renders the about page."""
    if 'selected_package' not in request.session:
        return redirect('/departments/')
    if request.method == 'POST':
        request.session['selected_doctor'] = {'doctor_name': request.POST['doctor_name'], 'doctor_surname': request.POST['doctor_surname']}
        return redirect('/doctor-detail/')
    print(request.session['selected_package'])
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/doctor-search.html',
        {
            'title': 'ค้นหาแพทย์'
        }
    )

def doctor_search_api(request):
    package_id = request.session['selected_package']
    days = request.GET.get('days').split(',') if request.GET.get('days') != None else None
    time = request.GET.get('time')
    doctor_firstname = request.GET.get('doctor_firstname')
    doctor_lastname = request.GET.get('doctor_surname')
    gender = request.GET.get('gender')
    status, result = api.find_doctors(package_id, days, time, doctor_firstname, doctor_lastname, gender)
    return JsonResponse({'status': status, 'result': result})

def doctor(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    status, result = api.show_doctor_in_department()
    return render(
        request,
        'app/doctor.html',
        {
            'title': 'แผนกและแพทย์',
            'departments': result
        }
    )


def confirm(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/confirm.html',
        {
            'title': 'ยืนยันแพ็คเกจ'
        }
    )


def payment(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payment.html',
        {
            'title': 'ชำระค่าบริการ'
        }
    )

def admin_mongo(request):
    assert isinstance(request, HttpRequest)
    status, result = api.get_all_collections_name()
    result.sort()
    return render(
        request,
        'app/admin-mongo.html',
        {
            'title': 'mongoDB Admin',
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
            'title': 'mongoDB Admin',
            'header_title': 'mongoDB Admin',
            'collection_name': collection_name,
            'data': result,
            'COLLECTION': True,
            'toolbar': True,
            'logo_link': '/admin-mongo'
        }
    )


