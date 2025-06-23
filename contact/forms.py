from django import forms
from .models import Contact, Order

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {'name': forms.TextInput(attrs={'input type': "text",
                                                  'class':"form-control mt-1",
                                                  'id':"name",
                                                  'name': "name",
                                                  'placeholder': "Name"}),

                   'email': forms.EmailInput(attrs={'input type': "email",
                                                    'class':"form-control mt-1",
                                                    'id': "email",
                                                    'name': "email",
                                                    'placeholder': "Email"}),

                   'subject': forms.TextInput(attrs={'input type': "text",
                                                     'class':"form-control mt-1",
                                                     'id': "subject",
                                                     'name': "subject",
                                                     'placeholder': "Subject"}),

                   'message': forms.Textarea(attrs={'class': "form-control mt-1",
                                                    'id': "message",
                                                    'name': "message",
                                                    'placeholder': "Message",
                                                    'rows': "8"})}

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['fullname', 'email', 'phone', 'adress']
        widgets = {'fullname': forms.TextInput(attrs={'input type':"text",
                                                      'name':"name",
                                                      'class':"form-control"}),

                   'email': forms.EmailInput(attrs={'input type':"email",
                                                    'name':"email",
                                                    'class':"form-control"}),

                   'phone': forms.TextInput(attrs={'input type':"tel",
                                                    'name':"phone",
                                                    'class':"form-control"}),

                   'adress': forms.Textarea(attrs={'textarea name': "address",
                                                   'class':"form-control"})}