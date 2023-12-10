# url_shortener_app/forms.py
from django import forms
from .models import URL

class ShortenURLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
