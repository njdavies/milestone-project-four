from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


class SignUpView(SuccessMessageMixin, CreateView):
    """View to display sign up page"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = 'Account created! A confirmation email has been sent to you separately.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Sign Up"
        context["title"] = title
        return context

    # A Confirmation email is sent to the user once an account has been created
    def form_valid(self, form):

        user = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')

        subject, from_email, to = 'Account creation', 'admin@artifactauctioneers.com', '{}'.format(
            email)
        text_content = render_to_string(
            'account_creation_text.txt', {'user': user})
        html_content = render_to_string(
            'account_creation.html', {'user': user})
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super().form_valid(form)
