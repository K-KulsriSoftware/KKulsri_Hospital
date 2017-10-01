"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


# class RegistrationForm(UserCreationForm):
#     # email = forms.EmailField(required=True)
#     # first_name = forms.TextInput()
#     # last_name = forms.TextInput()

#     class Meta:
#         model = User
#         fields = (
#             "username", 
#             "first_name", 
#             "last_name",
#             "email",
#             "password1", 
#             "password2"
#         )

#     def save(self, commit=True):
#         # Call save of the super of your own class,
#         # which is UserCreationForm.save() which calls user.set_password()
#         user = super(RegistrationForm, self).save(commit=False)

#         # Add the things your super doesn't do for you
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']

#         if commit:
#             user.save()

#         return user
