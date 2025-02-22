from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from unitor import views
from uposljena_jedinica.views import UposljenaJedinicaViewSet, StetaViewSet, trigger_error
from lokacije.views import LokacijeViewSet
from eksterni_oglasivaci.views import EksterniOglasivaciAPIView
from .views import  KorisnikViewSet

# Define the DefaultRouter
router = DefaultRouter()
router.register(r'korisnik', KorisnikViewSet, basename='korisnik')
router.register(r'uposljena_jedinica', UposljenaJedinicaViewSet, basename='uposljena_jedinica')
router.register(r'lokacije', LokacijeViewSet, basename='lokacije')
router.register(r'steta', StetaViewSet, basename='steta')

# Define urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # OAuth URLs for allauth
    path('api/', include(router.urls)),  # Include all registered viewsets
    path('api-auth/', include('rest_framework.urls')),
    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom endpoints for EksterniOglasivaci POST and PUT
    path('api/eksterni-oglasivaci/', EksterniOglasivaciAPIView.as_view(), name='eksterni_oglasivaci_post'),
    path('api/eksterni-oglasivaci/<int:pk>/', EksterniOglasivaciAPIView.as_view(), name='eksterni_oglasivaci_put'),
    path('sentry-debug/', trigger_error, name='sentry-debug'),
]
