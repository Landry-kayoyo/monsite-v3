
from django.contrib import admin
from django.urls import path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('article/<int:id>/<slug:slug>/', views.article_detail, name='article_detail'),
    path('services_list/', views.services_list, name='services_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
     path('contact/', views.contact, name='contact'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    