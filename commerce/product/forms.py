from django import forms

from .models import Product

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price', 'image')
        # widgets is a dictionary that contains the fields as keys and the widgets as values
        widgets = {
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            }),

        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        # widgets is a dictionary that contains the fields as keys and the widgets as values
        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            }),
        }
    #   populate the form with the current values of the product
    # def __init__(self, *args, **kwargs):
    #     super(EditProductForm, self).__init__(*args, **kwargs)
    #     self.fields['is_sold'].widget.attrs.update({'class': INPUT_CLASSES})

  