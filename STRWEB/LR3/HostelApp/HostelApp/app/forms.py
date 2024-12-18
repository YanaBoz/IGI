"""
Definition of forms.
"""

from datetime import timezone
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from app.models import Contact, About, Employee, Review, Review2
import re  # For phone number validation

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'rate', 'text', 'date']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['description', 'user', 'photo']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['contact','phone', 'email']
        
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['description', 'video', 'image', 'history', 'details', 'certificate']

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


class BootstrapRegistrationForm(UserCreationForm):
    """Registration form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    email = forms.EmailField(widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    age = forms.IntegerField(widget=forms.NumberInput({
                                   'class': 'form-control',
                                   'placeholder': 'Age'}))
    password2 = forms.CharField(label=_("Password confirmation"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password confirmation'}))

    class Meta:
        model = UserCreationForm.Meta.model
        fields = ('username', 'email', 'age')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2
    
    def clean_age(self):
        age = self.cleaned_data.get("age")    
        if age < 18:
            raise forms.ValidationError(_("Age must be 18 or older"))
        return age

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review2
        fields = ['rate', 'text']
        widgets = {
            'rate': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label='First Name')
    last_name = forms.CharField(max_length=50, required=True, label='Last Name')
    email = forms.EmailField(required=True, label='Email Address')
    phone_number = forms.CharField(max_length=20, required=True, label='Phone Number')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            # Implement your phone number validation logic here
            if not re.match(r'^\+\d{10,15}$', phone_number):
                raise forms.ValidationError('Please enter a valid phone number.')
        return phone_number

    address = forms.CharField(widget=forms.Textarea, required=True, label='Address')
    city = forms.CharField(max_length=50, required=True, label='City')
    zip_code = forms.CharField(max_length=10, required=True, label='Zip Code')
    country = forms.CharField(max_length=50, required=True, label='Country')