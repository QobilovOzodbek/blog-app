from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
