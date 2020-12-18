from django import forms
from django_countries.widgets import CountrySelectWidget

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'country', 'city', 'address', 'postcode')
        widgets = {'country': CountrySelectWidget()}

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'city': 'City',
            'address': 'Address',
            'postcode': 'Postal Code',
        }
        """Set the cursor to the full name field when the user loads the page"""
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style'
            # if field == 'country':
            #     self.fields[field].widget.attrs['class'] = 'select-wrapper'
            self.fields[field].label = False
