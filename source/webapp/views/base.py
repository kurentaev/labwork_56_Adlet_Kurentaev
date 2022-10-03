from django.shortcuts import render
from webapp.models import ProductsList
from webapp.models import StatusChoices


def index_view(request):
    products = ProductsList.objects.all()
    context = {
        "products": products,
        "choices": StatusChoices.choices
    }
    return render(request, "index.html", context)

