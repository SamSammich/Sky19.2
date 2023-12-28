from django import forms

from catalogapp.models import Product, Version

prohibited_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                   'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = ('name', 'description', 'price_for_one', 'avatar',)
        # fields = (' is_available')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in prohibited_list:
            if word in cleaned_data:
                raise forms.ValidationError(f"You should not use words like -->{prohibited_list}")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in prohibited_list:
            if word in cleaned_data:
                raise forms.ValidationError(
                    f"You should not use words like -->{prohibited_list}")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    def clean_is_active(self):
        cleaned_data = self.cleaned_data.get('is_active')
        # print(self.__dict__)
        if cleaned_data:
            version = self.cleaned_data['product'].version_set.filter(is_active=True)
            if version:
                raise forms.ValidationError('Error, Product already has active version!')
                # for vers in version:   #  это вариант с удалением активности остальных версий
                #    vers.is_active = False  #  при включении новой активной версии
                #    vers.save()
        return cleaned_data
