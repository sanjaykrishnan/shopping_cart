from django.views.generic import TemplateView


class ProductListView(TemplateView):
    template_name = 'cart/product-list.html'


class ProductDetailView(TemplateView):
    template_name = 'cart/product-detail.html'


class CartView(TemplateView):
    template_name = 'cart/cart.html'
