from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order
from products.models import Product
from django.conf import settings
from django.utils import timezone
from products.models import Product
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            address = order

            cart = request.session.get('cart', {})
            total = 0
            products = []

            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += product.buyout_price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product
                )
                order_line_item.save()
                product.status = 'Closed'
                product.save()
                products.append(product)

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(
                    request, "Payment received! Email confirmation has been sent to you separately.")
                request.session['cart'] = {}

                # A Confirmation email is sent the user once payment has been made
                user = request.user
                email = request.user.email

                subject, from_email, to = 'Payment confirmation', 'admin@artifactauctioneers.com', '{}'.format(
                    email)
                text_content = render_to_string(
                    'checkout_email_text.txt', {'user': user, 'products': products, 'address': address, 'total': total})
                html_content = render_to_string(
                    'checkout_email.html', {'user': user, 'products': products, 'address': address, 'total': total})
                msg = EmailMultiAlternatives(
                    subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
