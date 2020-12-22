from django import forms
from django_countries.widgets import CountrySelectWidget
from checkout.models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('country', 'address','town', 'zip_code', 'mobail')
        widgets = {'country': CountrySelectWidget({
            'class':'form-control'
        })}