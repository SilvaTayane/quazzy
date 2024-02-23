from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app_quazzy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home' ),
    path('profile/', views.profile, name = 'profile' ),
    path('trending/', views.trending, name = 'trending' ),
    path('new_friend/', views.new_friend, name = 'new-friend' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.MEDIA_ROOT)
