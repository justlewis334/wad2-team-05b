"""poemgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from registration.backends.simple.views import RegistrationView

## There's really no good place for this

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request):
        return "poemApp:index"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('poemApp/', include(('poemApp.urls', 'poemApp'), namespace="poemApp")),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/favicon.png'))),
    path('accounts/register/', MyRegistrationView.as_view(), name="registration_register"),
    path('accounts/', include('registration.backends.simple.urls')),
]
