from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), {'title': 'Home'}, name='home'),
    path('about/', AboutPageView.as_view(), {'title': 'About'}, name='about'),
    path('contact/', ContactPageView.as_view(),
         {'title': 'Contact Us'}, name='contact'),
]
