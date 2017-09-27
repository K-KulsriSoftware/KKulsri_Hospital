"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

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
    return render(
        request,
        'app/doctor-detail.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )


def register(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/register.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
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
    return render(
        request,
        'app/departments.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )


def regular_packages(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/regular-package.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
    )


def special_packages(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/special_packages.html',
        # {
        #     'title': 'About',
        #     'message': 'Your application description page.',
        #     'year': datetime.now().year,
        # }
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
