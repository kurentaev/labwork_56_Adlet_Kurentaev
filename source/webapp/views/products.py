from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import ProductsList
from webapp.models import StatusChoices
# from webapp.forms import TasksListForm


def product_view(request, pk):
    product = get_object_or_404(ProductsList, pk=pk)
    return render(request, 'product.html', context={'product': product, "choices": StatusChoices.choices})

