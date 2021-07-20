from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_username(self):
        cd = self.cleaned_data
        user = cd['username'].capitalize()
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('User already exists')
        return user

    def clean_email(self):
        cd = self.cleaned_data
        email = cd['email'].capitalize()
        if email == "":
            return email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail already exists')
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        cd = self.cleaned_data
        return cd['username'].capitalize()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        cd = self.cleaned_data
        email = cd['email'].capitalize()
        if email=='' or self.instance.email==email:
            return email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail already exists')
        return email

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',)
