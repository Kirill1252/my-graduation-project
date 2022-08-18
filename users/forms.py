from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'mobile')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'instagram', 'mobile', 'facebook')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email address',
                               widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                             'type': 'email',
                                                             'aria-describedby': 'emailHelp',
                                                             }))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                                               'type': 'password',
                                                                               'aria-describedby': 'emailHelp',
                                                                               }))


class RegisterUserForm(CustomUserCreationForm):
    username = forms.EmailField(label='Email address',
                                widget=forms.EmailInput(attrs={'class': 'form-label form-control mb-3',
                                                               'type': 'email',
                                                               'aria-describedby': 'emailHelp',
                                                               'placeholder': 'name@example.com'
                                                               }))

    password1 = forms.CharField(label='Password ',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-label mb-3',
                                                                  'type': 'password',
                                                                  'aria-describedby': 'emailHelp',
                                                                  }))

    password2 = forms.CharField(label='Password confirmation ',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-label mb-3',
                                                                  'type': 'password',
                                                                  'aria-describedby': 'emailHelp',
                                                                  }))
    mobile = forms.IntegerField(label='Mobile', widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                                              'type': 'tel',
                                                                              }))
    first_name = forms.CharField(label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                               'type': 'text',
                                                               'aria-describedby': 'emailHelp',
                                                               }))
    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                              'type': 'text',
                                                              'aria-describedby': 'emailHelp',
                                                              }))

    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2',
            'mobile', 'first_name', 'last_name',
        )


class UpdateUserData(CustomUserChangeForm):
    mobile = forms.IntegerField(label='Mobile', widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                                              'type': 'tel',
                                                                              }))
    first_name = forms.CharField(label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                               'type': 'text',
                                                               'aria-describedby': 'emailHelp',
                                                               }))
    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                              'type': 'text',
                                                              'aria-describedby': 'emailHelp',
                                                              }))
    avatar = forms.CharField(label='Avatar',
                             widget=forms.FileInput(attrs={'class': 'form-control form-label mb-3',
                                                           'type': 'file',
                                                           'aria-describedby': 'emailHelp',
                                                           }))
    instagram = forms.CharField(label='Instagram',
                                widget=forms.URLInput(attrs={'class': 'form-control form-label mb-3',
                                                             'type': 'url',
                                                             'aria-describedby': 'emailHelp',
                                                             }))
    facebook = forms.CharField(label='Facebook',
                               widget=forms.URLInput(attrs={'class': 'form-control form-label mb-3',
                                                            'type': 'url',
                                                            'aria-describedby': 'emailHelp',
                                                            }))

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'avatar',
            'instagram', 'facebook', 'mobile'
        )
