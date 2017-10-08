"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
# from app.models import Profile

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



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class RegistrationForm(UserCreationForm):
    username = forms.RegexField(
        label=_("ชื่อผู้ใช้"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=_("จำเป็นต้องกรอก. ไม่เกิน 30 ตัวอักษร ประกอบด้วย พยัญชนะ, ตัวเลข หรือ "
                    "@/./+/-/_ เท่านั้น"),
        error_messages={
            'invalid': _("ชื่อผู้ใช้ ต้องประกอบด้วย พยัญชนะ, ตัวเลข หรือ "
                         "@/./+/-/_ เท่านั้น")},
    )
    password1 = forms.CharField(
        label=_("รหัสผ่าน"),widget=forms.PasswordInput,)
    password2 = forms.CharField(
        label=_("พิมพ์รหัสผ่านอีกครั้ง"),widget=forms.PasswordInput,)
    first_name = forms.CharField(
        label=_("ชื่อ"), required=True, max_length=30, help_text="Required")
    last_name = forms.CharField(
        label=_("นามสกุล"), required=True, max_length=30, help_text="Required")
    email = forms.EmailField(
        label=_("อีเมล"), required=True, max_length=100, help_text="Required")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


#     patient_name_title = forms.CharField()
#     patient_name = forms.CharField()
#     patient_surname = forms.CharField()
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
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
    # email = forms.EmailField()
#     congenital_disease = forms.CharField()

    # class Meta:
    #     model = User
    #     fields = ('username', 'password1', 'password2', "birth_date",)
#         fields = ('username', 'password1', 'password2', "patient_name_title", "patient_name", "patient_surname", "birth_date", "patient_img",
#                   "id_card_number", "gender", "blood_group_abo", "blood_group_rh",
#                   "race", "nationallity", "Religion", "Status", "pateint_address",
#                   "occupy", "telphone_number", "father_name", "mother_name",
#                   "emergency_name", "emergency_phone", "emergency_addr", "email", "congenital_disease")
