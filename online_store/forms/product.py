from django import forms
from django.core.exceptions import ValidationError

from online_store.models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'category': 'Категория',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите описание товара'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'}),
        }

    def clean_name(self):
        """Кастомная валидация названия товара (name)."""
        name = self.cleaned_data.get('name')
        if len(name) < 5:
            raise ValidationError('Название должен содержать минимум 5 символов')
        return name

    def clean_description(self):
        """Кастомная валидация описания товара (description)."""
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise ValidationError('Описание должно содержать минимум 10 символов.')
        return description

    def clean_price(self):
        """Кастомная валидация цены (price)."""
        price = self.cleaned_data.get('price')
        if price is not None:
            if price < 0:
                raise ValidationError('Цена не может быть отрицательной.')
            elif price == 0:
                raise ValidationError('Цена не может быть равна нулю.')
        return price

    def clean_category(self):
        """Кастомная валидация категории (category)."""
        category = self.cleaned_data.get('category')
        if category.name == 'Без категории':
            raise ValidationError('Товар не может быть в категории "Без категории".')
        return category

    def clean(self):
        """Общая валидация."""
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and description and name.lower() in description.lower():
            raise ValidationError('Название не должно повторяться в описании.')

        return cleaned_data


class ProductDeleteForm(forms.Form):
    """Форма для подтверждения удаления товара."""
    confirm = forms.BooleanField(
        required=True,
        label='Подтвердите удаление',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
