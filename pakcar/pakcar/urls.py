from django.contrib import admin
from django.urls import path
from car import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('contact/', views.ContactPage, name='contact'),
    path('about/', views.AboutPage, name='about'),
    path('product/', views.ProductPage, name='product'),
    path('sproduct/', views.SingleProduct, name='sproduct')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
