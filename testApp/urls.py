from django.contrib import admin
from django.urls import path
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', views.one),
    path('two/', views.two),
    path('three/', views.three),
    path('four/', views.four),
    path('five/', views.five),
]