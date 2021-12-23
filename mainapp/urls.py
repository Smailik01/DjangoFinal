from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('events/', events, name='events'),
    path('teachers/', teachers, name='teachers'),
    path('contact/', contact, name='contact'),
    # path('signup/', signup, name='signup'),
    path('register/', register, name='register'),
]