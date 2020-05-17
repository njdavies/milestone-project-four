from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    """View to display Home page"""
    template_name = 'index.html'


class AboutPageView(TemplateView):
    """View to display About page"""
    template_name = 'about.html'


class ContactPageView(TemplateView):
    """View to display Contact page"""
    template_name = 'contact.html'
