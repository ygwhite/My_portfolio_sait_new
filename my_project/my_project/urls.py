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
from django.contrib import admin
from django.urls import path, include, re_path as url
from rest_framework.routers import SimpleRouter
from orders.views import orders_page, OrderView, orders_app
from store.views import ClothesView, auth, UserClothesRelationsView

router = SimpleRouter()

router.register(r'clothes', ClothesView)
router.register(r'clothes_relation', UserClothesRelationsView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    url('', include('social_django.urls', namespace='social')),
    path('orders_page/', orders_app),
    path('auth/', auth),

]

urlpatterns += router.urls
