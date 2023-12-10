from django.shortcuts import render

# Create your views here.
# url_shortener_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import ShortenURLForm

def home(request):
    form = ShortenURLForm(request.POST or None)
    if form.is_valid():
        url_object, created = URL.objects.get_or_create(original_url=form.cleaned_data['original_url'])

        return render(request, 'url_shortener_app/success.html', {'url_object': url_object})
    return render(request, 'url_shortener_app/home.html', {'form': form})

def redirect_original(request, short_code):
    url_object = get_object_or_404(URL, short_code=short_code)
    return redirect(url_object.original_url)
