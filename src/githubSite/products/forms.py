from django import forms
from .models import Product

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False,
                    widget=forms.TextInput(
                        attrs={
                            "class": "new-class-name two",
                            "id": "my_id_textarea",
                            "rows": 20,
                            "cols": 120,
                            "placeholder": "Your description"
                        }
                    )
        )
    price = forms.DecimalField(initial=199.99)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]