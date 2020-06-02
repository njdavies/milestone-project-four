from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, contact_form

urlpatterns = [
    path('', HomePageView.as_view(), {'title': 'Home'}, name='home'),
    path('about/', AboutPageView.as_view(), {'title': 'About'}, name='about'),
    path('contact/', ContactPageView.as_view(),
         {'title': 'Contact Us'}, name='contact'),
    path('contact/form/', contact_form, name='contact_form'),
]
