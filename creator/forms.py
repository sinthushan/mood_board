from django import forms


class Register(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput)