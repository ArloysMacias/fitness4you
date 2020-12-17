from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # To include all fields
        fields = ('product_name', 'category', 'price', 'verified_buyer_rating', 'brand_name', 'product_description')
        # fields = '__all__'

    # To make changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

        # for c in categories:
        #     friendly_names = (c.id, c.get_friendly_name())

        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names.insert(0, (0, 'Category *'))

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.label = False
                # if field == 'country':
                #     self.files[field].widget.attrs['class'] = 'grey-text'
            if field_name == 'product_description':
                field.widget.attrs['data-length'] = '120'
                field.widget.attrs['class'] = 'materialize-textarea'
