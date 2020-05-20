from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import redirect, reverse
from .models import Product, Bid
from django.shortcuts import render
from datetime import datetime
from django.db.models import Max
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class AllProductsView(ListView):
    """
    A view to display a list of all products 
    """
    model = Product
    template_name = "products.html"
    context_object_name = "Products"
    paginate_by = 4

    # Additional context information passed to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Products"
        context["title"] = title
        return context

    # The queryset is overridden to return only products with a status of 'Open'
    def get_queryset(self):
        return Product.objects.filter(status='Open')


class SortedProductsView(ListView):
    """
    A view to display a sorted list of products 
    """
    model = Product
    template_name = "products.html"
    context_object_name = "Products"

    # The queryset is overridden to return products as specified by the sort filter
    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.GET.get("sort"):
            selection = self.request.GET.get("sort")
            if selection == "end_date":
                queryset = Product.objects.filter(
                    status='Open').order_by('end_date')
            elif selection == "starting_price":
                queryset = Product.objects.filter(status='Open').order_by(
                    'starting_price').reverse()
        return queryset


class EraListView(ListView):
    """
    A view to display a list of products from a specific era
    """
    template_name = "specific_products.html"
    context_object_name = "Products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Products"
        context["title"] = title
        return context

    # The queryset is overridden to return only products with a status
    #  of 'Open' that matches the specific era
    def get_queryset(self):
        return Product.objects.filter(era=self.kwargs['era'], status='Open')


def artifact_detail(request, pk):
    """
    A view to display a specific product
    """
    product = Product.objects.get(id=pk)
    bid = Bid.objects.filter(name=product).aggregate(Max('current_bid'))
    bids = Bid.objects.filter(name=product.name).order_by('-current_bid')

    # If a bid is made the details are sent to the database and a confirmation
    # message is displayed to the suer
    if request.method == 'POST':
        new_bid = Bid()
        new_bid.name = product.name
        new_bid.product = product
        new_bid.current_bid = request.POST.get('bid')
        new_bid.current_bid_user = request.user
        new_bid.current_bid_date = datetime.now()
        new_bid.save()
        messages.success(
            request, 'Bid received! Email confirmation has been sent to you separately.')

        # A Confirmation email is sent the user once a bid has been made
        user = request.user
        email = request.user.email

        subject, from_email, to = 'Bid confirmation', 'admin@artifactauctioneers.com', '{}'.format(
            email)
        text_content = render_to_string(
            'bid_email_text.txt', {'user': user, 'product': product, 'new_bid': new_bid})
        html_content = render_to_string(
            'bid_email.html', {'user': user, 'product': product, 'new_bid': new_bid})
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponseRedirect(request.path_info)
    else:
        return render(request, 'artifact.html', {'product': product, 'bid': bid, 'bids': bids})
