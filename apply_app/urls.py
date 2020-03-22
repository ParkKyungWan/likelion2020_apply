from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [
    path('',views.confirm,name="apply"),
    path('foradmin/',views.check_apply, name="check_apply"),
    path('foradmin/<int:applier_id>/delete', views.delete_applier,name='delete'),
    path('foradmin/applier/<int:applier_id>', views.applier, name="applier"),
]