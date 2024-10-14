from django.urls import path
from .import views
from django.conf import settings 
from django.conf.urls.static import static
from .views import custom_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('elements/', views.elements, name= 'elements'),
    path('staff/', views.staff, name= 'staff'),
    path('news/', views.news, name= 'news'),
    path('gallery/', views.gallery, name= 'gallery'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact_us'),
    path('register/', views.register, name= 'register'),
    path('login/', views.user_login, name= 'login'),
    path('logout/', custom_logout, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('course_details/<int:id>', views.course_details, name='course_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)