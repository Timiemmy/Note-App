from django import forms
from .models import CustomUser, Profile



class UserUpdateViewForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'address', 'phone_number']