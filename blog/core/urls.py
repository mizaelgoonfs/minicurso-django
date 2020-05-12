from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.detail, name='detail'),
    path('about', views.about, name='about'),

]
