from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_short_url, name='create'),
    path('<str:short_url>', views.redirect_to_original, name='redirect'),
]