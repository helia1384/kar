"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from dash import views
from products import cart
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),



    # اپ داشبورد (اصلی)
    path('', include('dash.urls')),

    # اپ محصولات
    path('products/', include('products.urls')),


    path('cart/', cart.cart_view, name='cart_view'),
    path('add/<int:product_id>/', cart.add_to_cart, name='add_to_cart'),
    path('update/<int:product_id>/<str:action>/', cart.update_cart, name='update_cart'),    path('account/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),

]

# برای فایل‌های استاتیک (css, js, ...)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# برای فایل‌های مدیا (عکس‌های آپلودی)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

