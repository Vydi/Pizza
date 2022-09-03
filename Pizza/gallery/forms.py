from django import forms


class ContactForm(forms.Form):
    user_name = forms.CharField(label='Имя',
                                widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ваше имя"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Введите существующий email"
        }))
    content = forms.CharField(label='Текст', widget=forms.Textarea(
        attrs={'class': 'form-control', "rows": 5, "placeholder": "Сообщение..."}))
