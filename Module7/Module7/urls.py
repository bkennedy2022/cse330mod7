"""Module7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from website.views import logout_request
#from website.views import welcome
from website.views import wordSearch, register, registering
from django.urls import path, include
from django.views.generic.base import TemplateView

# from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from myweblab import settings

# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls), #first argument is the url, second is the view function
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', register, name = 'register'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('word_lookup', wordSearch),
    path('accounts/registering', registering)
]  #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
