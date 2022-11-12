from django import forms


class GuestForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Имя Автор')
    email = forms.EmailField(max_length = 150, required=True, label='Почта')
    description = forms.CharField(max_length=400, required=True, label='Текст')