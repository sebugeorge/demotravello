from . import views
from django.urls import path

# STATIC
urlpatterns = [
     path('',views.demo, name='demo')
 ]