# account/forms.py

from django import forms
from django.contrib.auth import (authenticate, get_user_model)

User = get_user_model()


class SignInForm(forms.Form):
    username = forms.fields.CharField(max_length=20)
    password = forms.fields.CharField(max_length=20,
                                      widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            authenticate_user = authenticate(
                username=username, password=password)
            print(username, password, authenticate_user)
            if authenticate_user is None:

                raise forms.ValidationError('This user does not exist')
                raise forms.ValidationError("invalid password")
            else:
                return

        return super(SignInForm, self).clean(*args, **kwargs)


class SignUpForm(forms.ModelForm):
    username = forms.fields.CharField(max_length=20)
    password = forms.fields.CharField(max_length=20,
                                      widget=forms.PasswordInput)
    confirm_password = forms.fields.CharField(
        max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'confirm_password'
        ]

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            print("Password must match")
            raise forms.ValidationError("Password must match")

        return super(SignUpForm, self).clean(*args, **kwargs)
