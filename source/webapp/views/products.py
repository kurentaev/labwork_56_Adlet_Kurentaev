from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import ProductsList
from webapp.models import StatusChoices
from webapp.forms import ProductsListForm


def product_view(request, pk):
    product = get_object_or_404(ProductsList, pk=pk)
    return render(request, 'product.html', context={'product': product, "choices": StatusChoices.choices})


def add_view(request):
    if request.method == "GET":
        form = ProductsListForm()
        return render(request, "product_add.html", context={'form': form})
    elif request.method == "POST":
        form = ProductsListForm(request.POST)
        if form.is_valid():
            product_data = {
                'title': request.POST.get('title'),
                'description': request.POST.get('description'),
                'image': request.POST.get('image'),
                'category': request.POST.get('category'),
                'rest': request.POST.get('rest'),
                'price': request.POST.get('price'),
            }
            product = ProductsList.objects.create(**product_data)
            return redirect('product_detail', pk=product.pk)

