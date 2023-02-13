"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
# from orders.views import orders_page, OrderView, orders_app
from orders.views import orders_app
from store.views import ClothesView, UserClothesRelationsView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import CartViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart')

router = SimpleRouter()

router.register(r'clothes', ClothesView)
router.register(r'clothes_relation', UserClothesRelationsView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('orders_page/', orders_app),
    path('api/cart/', include(router.urls))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
