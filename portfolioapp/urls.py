from django.urls import path

from .views import index,contact
                                                                                                             
app_name = "profile"

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
]