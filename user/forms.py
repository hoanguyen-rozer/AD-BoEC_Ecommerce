from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :')
    email = forms.EmailField(max_length=200, label='Email :')
    first_name = forms.CharField(
        max_length=100, label='First Name:')
    last_name = forms.CharField(
        max_length=100, label='Last Name:')
    password1 = forms.CharField(max_length=30, label='Password :')
    password2 = forms.CharField(max_length=30, label='Password Confirmation :')

    username.widget = forms.TextInput(attrs={'size': 50, 'class': 'form-control'})
    email.widget = forms.TextInput(attrs={'size': 50, 'class': 'form-control'})
    first_name.widget = forms.TextInput(attrs={'size': 50, 'class': 'form-control'})
    last_name.widget = forms.TextInput(attrs={'size': 50, 'class': 'form-control'})
    password1.widget = forms.PasswordInput(attrs={'size': 50, 'class': 'form-control'})
    password2.widget = forms.PasswordInput(attrs={'size': 50, 'class': 'form-control'})
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', )


class UserUpdateForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        readonly_fields = ('username', )
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Hanoi', 'Hanoi'),
    ('Da Nang', 'Da Nang'),
    ('HCM City', 'HCM City'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }
