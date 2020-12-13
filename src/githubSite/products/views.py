from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        "object_list": queryset
    }    
    return render(request, "product/list.html", context)



def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }    
    return render(request, "product/delete.html", context)

def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=1)
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "product/detail.html", context)

def product_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST or None)
        if form.is_valid():
            #now the data is good
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "product/create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id = 1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }

    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)