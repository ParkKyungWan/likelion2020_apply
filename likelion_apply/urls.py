"""likelion_apply URL Configuration

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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import apply_app.views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',apply_app.views.home,name="home"),
    path('apply/',apply_app.views.apply,name="apply"),
    path('apply/confirm/', apply_app.views.confirm, name='confirm'),
    path('foradmin/', apply_app.views.check_apply, name="check_apply"),
    path('foradmin/<int:applier_id>/delete', apply_app.views.delete_applier,name='delete'),
    path('foradmin/applier/<int:applier_id>', apply_app.views.applier, name="applier"),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
