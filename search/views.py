from django.views.generic import ListView
from products.models import Product


class SearchView(ListView):
    """
    A view which returns a single result or list of results that
    match the search query
    """
    model = Product
    template_name = "products-search.html"
    context_object_name = "Products"
    paginate_by = 4

    # Queryset is overridden to only return products with a status of 'Open'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                name__icontains=query, status='Open')
        else:
            object_list = self.model.objects.none()
        return object_list
