from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    username = forms.CharField(max_length = 50)
    email = forms.EmailField(label = 'E-Mail')
    phone_number = forms.IntegerField()
    role = forms.CharField(max_length = 10)