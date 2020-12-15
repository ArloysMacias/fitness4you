from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        # fields = ('full_name', 'email', 'phone_number', 'country', 'city', 'address', 'postcode')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name_default': 'Full Name',
            'email_default': 'Email Address',
            'phone_number_default': 'Phone Number',
            'city_default': 'City',
            'address_default': 'Address',
            'postcode_default': 'Postal Code',
        }
        """Set the cursor to the full name field when the user loads the page"""
        self.fields['full_name_default'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'country_default':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # self.fields[field].widget.attrs['class'] = 'stripe-style'
            self.fields[field].label = False
