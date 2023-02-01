from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from .models import ProductsCategory, Product, Basket_pro


def index(request):

    context = {
        "title": "Artemio store",
        "is_prom": True,
    }
    return render(request, "products/index.html", context)


def products(request):

    context = {
        "title": "Product catalog",
        'products': Product.objects.all(),
        "categories": ProductsCategory.objects.all(),
    }
    return render(request, "products/products.html", context)


@login_required
def basket_add(request, products_id):
    product = Product.objects.get(id=products_id)
    baskets = Basket_pro.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket_pro.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_remove(request, basket_id):
    basket = Basket_pro.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])