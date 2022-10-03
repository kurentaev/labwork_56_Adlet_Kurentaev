from django.shortcuts import render
from webapp.models import ProductsList
from webapp.models import StatusChoices
from webapp.forms import ProductsSearchForm


def index_view(request):
    form = ProductsSearchForm()
    if request.method == 'GET' and 'title' in request.GET:
        title = request.GET['title']
        products = ProductsList.objects.filter(title=title)
    else:
        products = ProductsList.objects.filter(rest__gte=1).order_by('category', 'title')
    context = {
        "products": products,
        "choices": StatusChoices.choices,
        "form": form
    }
    return render(request, "index.html", context)
