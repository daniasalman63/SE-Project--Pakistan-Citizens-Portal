from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
import re

class CNICField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.regex = re.compile(r'^\d{5}-\d{7}-\d{1}$')
        self.error_messages['invalid'] = 'Enter a valid CNIC number in the format XXXXX-XXXXXXX-X'
    
    def clean(self, value):
        value = super().clean(value)
        if not self.regex.match(value):
            raise forms.ValidationError(self.error_messages['invalid'])
        return value

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    # cnic = forms.CharField(max_length=15, help_text='Required. Add a valid CNIC')
    CNIC = CNICField(max_length=15, help_text='Required. Add a valid CNIC in the format XXXXX-XXXXXXX-X')
    
    class Meta:
        model = Account
        # fields = ("email", "username", "password1", "password2", "cnic")
        fields = ("email", "CNIC", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    CNIC = forms.CharField(max_length=13, min_length=13, label='CNIC', widget=forms.TextInput(attrs={'placeholder': 'XXXXX-XXXXXXX-X'}))

    class Meta:
        model = Account
        fields= ('email', 'CNIC', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            CNIC = self.cleaned_data['CNIC']
            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError("Invalid login credentials")
            elif not user.check_cnic(CNIC):
                raise forms.ValidationError("Invalid CNIC")

        return self.cleaned_data