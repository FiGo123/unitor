from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from unitor import views
from unitor.views import EksterniOglasivaciAPIView

# Define the DefaultRouter
router = DefaultRouter()
router.register(r'korisnik', views.KorisnikViewSet)
router.register(r'uposljena_jedinica', views.UposljenaJedinicaViewSet)
router.register(r'pomocni_radnici', views.PomocniRadniciViewSet)
router.register(r'lokacije', views.LokacijeViewSet)
router.register(r'eksterni_oglasivaci', views.EksterniOglasivaciViewSet)
router.register(r'steta', views.StetaViewSet)

# Define urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # OAuth URLs for allauth
    path('api/', include(router.urls)),

    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom endpoints for EksterniOglasivaci POST and PUT
    path('api/eksterni-oglasivaci/', EksterniOglasivaciAPIView.as_view(), name='eksterni_oglasivaci_post'),
    path('api/eksterni-oglasivaci/<int:pk>/', EksterniOglasivaciAPIView.as_view(), name='eksterni_oglasivaci_put'),
]
