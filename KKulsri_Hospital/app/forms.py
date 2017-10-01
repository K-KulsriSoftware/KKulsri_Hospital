"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Profile

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


# class RegistrationForm(UserCreationForm):
#     patient_name_title = forms.CharField()
#     patient_name = forms.CharField()
#     patient_surname = forms.CharField()
#     birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
#     patient_img = forms.ImageField()
#     id_card_number = forms.CharField()
#     gender = forms.CharField()
#     blood_group_abo = forms.CharField()
#     blood_group_rh = forms.CharField()
#     race = forms.CharField()
#     nationallity = forms.CharField()
#     Religion = forms.CharField()
#     Status = forms.CharField()
#     pateint_address = forms.CharField()
#     occupy = forms.CharField()
#     telphone_number = forms.CharField()
#     father_name = forms.CharField()
#     mother_name = forms.CharField()
#     emergency_name = forms.CharField()
#     emergency_phone = forms.CharField()
#     emergency_addr = forms.CharField()
#     email = forms.EmailField()
#     congenital_disease = forms.CharField()

#     class Meta:
#         model = User
        
#         fields = ('username', 'password1', 'password2', "patient_name_title", "patient_name", "patient_surname", "birth_date", "patient_img",
#                   "id_card_number", "gender", "blood_group_abo", "blood_group_rh",
#                   "race", "nationallity", "Religion", "Status", "pateint_address",
#                   "occupy", "telphone_number", "father_name", "mother_name",
#                   "emergency_name", "emergency_phone", "emergency_addr", "email", "congenital_disease")
