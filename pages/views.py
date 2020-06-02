from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class HomePageView(TemplateView):
    """View to display Home page"""
    template_name = 'index.html'


class AboutPageView(TemplateView):
    """View to display About page"""
    template_name = 'about.html'


class ContactPageView(TemplateView):
    """View to display Contact page"""
    template_name = 'contact.html'


def contact_form(request):
    """
    Confirmation emails sent to site admin and user when contact form is submitted
    """
    if request.method == 'POST':
        user = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('subject')
        message = request.POST.get('message')

        # Email to site admin
        subject, from_email, to = 'Contact Form Submission', 'admin@artifactauctioneers.com', 'nathandavies06@hotmail.co.uk',
        text_content = render_to_string(
            'contact_form_admin_text.txt', {'user': user, 'email': email, 'title': title, 'message': message})
        html_content = render_to_string(
            'contact_form_admin.html', {'user': user, 'email': email, 'title': title, 'message': message})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # Email to user
        subject, from_email, to = 'Contact Form Submission', 'admin@artifactauctioneers.com', '{}'.format(
            email)
        text_content = render_to_string(
            'contact_form_user_text.txt', {'user': user, 'title': title, 'message': message})
        html_content = render_to_string(
            'contact_form_user.html', {'user': user, 'title': title, 'message': message})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(
            request, 'Thank you for your query! Our team will be in touch shortly.')
        return render(request, 'contact.html')
