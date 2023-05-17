from django import forms

from news_list.models import News


class NewsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'текст'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)

    preview = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)
