from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    """View to display sign up page"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Sign Up"
        context["title"] = title
        return context
