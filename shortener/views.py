from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from .models import ShortenedLink
from .forms import URLInputForm

def create_short_url(request):
    if request.method == 'POST':
        form = URLInputForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['url']
            ip = request.META['REMOTE_ADDR']
            user_agent = request.META['HTTP_USER_AGENT']
            short_link = ShortenedLink(link=link, user_ip=ip, user_agent=user_agent)
            short_link.save()
            return render(request, 'shortener/result.html', {'shortened_link': short_link.shortened_link})
    else:
        form = URLInputForm()
    return render(request, 'shortener/index.html', {'form': form})

def redirect_to_original(request, short_url):
    try:
        link = ShortenedLink.objects.get(shortened_link=short_url)
    except ShortenedLink.DoesNotExist:
        messages.error(request, "The link does not exist.")
        return redirect('shortener:create')
    if timezone.now() - link.creation_date > timedelta(days=7):
        messages.error(request, "The link does not exist.")
        return redirect('shortener:create')
    return redirect(link.link)
