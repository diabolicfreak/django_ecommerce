from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField()
    content = forms.Textarea()

    def clean_email(self):
        print("asdasd")
        email = self.cleaned_data.get('email')
        if "gmail" not in email:
            raise forms.ValidationError("Has to be a gmail account")
        return email 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already taken")
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError("Passwords dont match")
        return self.cleaned_data