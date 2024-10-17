from django import forms

from . models import Payment

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['user', 'room']
        fields = ('user', 'amount', 'payment_method')
        widgets = {
            'user': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'amount': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'payment_method': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }
