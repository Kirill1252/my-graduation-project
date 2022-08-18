from django import forms

from .models import Orders, AnonymousFormOrders


class OrdersForm(forms.ModelForm):
    additional_information = forms.CharField(label='Additional contacts',
                                             widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                                           'type': 'text',
                                                                           'aria-describedby': 'emailHelp',
                                                                           }))

    class Meta:
        model = Orders
        fields = ('additional_information',)


class AnonymousFormOrdersForms(forms.ModelForm):
    name = forms.CharField(label='Name',
                           widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                         'type': 'text',
                                                         'aria-describedby': 'emailHelp',
                                                         }))
    email = forms.CharField(label='Email address',
                            widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                          'type': 'email',
                                                          'aria-describedby': 'emailHelp',
                                                          }))
    mobile = forms.IntegerField(label='Mobile', widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                                              'type': 'tel',
                                                                              }))

    class Meta:
        model = AnonymousFormOrders
        fields = ('name', 'mobile', 'email')


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject',
                              widget=forms.TextInput(attrs={'class': 'form-control form-label mb-3',
                                                            'type': 'text',
                                                            'aria-describedby': 'emailHelp',
                                                            }))
    content = forms.CharField(label='Content',
                              widget=forms.Textarea(attrs={'class': 'form-control form-label mb-3',
                                                           'type': 'text',
                                                           'aria-describedby': 'emailHelp',
                                                           }))
