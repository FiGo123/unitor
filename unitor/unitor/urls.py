"""
URL configuration for unitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from your_app import views  # Update 'your_app' with the correct app name

router = DefaultRouter()
router.register(r'korisnik', views.KorisnikViewSet)
router.register(r'uposljena_jedinica', views.UposljenaJedinicaViewSet)
router.register(r'pomocni_radnici', views.PomocniRadniciViewSet)
router.register(r'lokacije', views.LokacijeViewSet)
router.register(r'eksterni_oglasivaci', views.EksterniOglasivaciViewSet)
router.register(r'steta', views.StetaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Add the OAuth allauth routes
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for OAuth

    # API routes
    path('api/', include(router.urls)),
]
