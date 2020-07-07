"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('contact/', include(('contact.urls', 'contact'),
                             namespace='contact')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('checkout/',
         include(('checkout.urls', 'checkout'), namespace='checkout')),
    path('likes/', include(('likes.urls', 'likes'), namespace='likes')),
    path('', include(('products.urls', 'products'), namespace='products')),
    path('users/', include(('users.urls', 'users'),
                           namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
