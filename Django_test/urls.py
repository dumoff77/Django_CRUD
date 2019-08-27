
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

#from phone_handbook.views import HandBookView
from phone_handbook import views



urlpatterns = [
    #path('api/v1/handbook/', include('phone_handbook.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/handbook/', views.handbook_list),
    path('api/v1/handbook/<str:name>', views.handbook_by_name)
]