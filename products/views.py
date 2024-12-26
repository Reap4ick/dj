from django.http import HttpResponse
from django.shortcuts import redirect, render

from products.forms.create import CreateProduct
from products.forms.edit import EditProduct
from products.models import Product



# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})
def list(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})



def details(request, id):
    try:
        product = Product.objects.get(pk=id)
        print(product)
        return render(request, "detail.html", {"product": product})
    except:
        error="Product not except"
        return render(request, "detail.html", {"error": error})
    
    # return render(request, "detail.html", {"product": product, "error": error})


def delete(request, id):
    product = Product.objects.get(pk=id)

    if product is None:
        return HttpResponse("User not found")
    
    product.delete()
    
    return redirect("/products/home")


def create(request):

    form = CreateProduct()

    if request.method == "POST":
        form = CreateProduct(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/products/list")

    return render(request, "create.html", {"form": form})



def edit(request, id):

    product = Product.objects.get(id=id)

    if product is None:
        return HttpResponse("User not found")

    form = EditProduct(instance=product)

    if request.method == "POST":
        form = CreateProduct(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("/products/list")

    return render(request, "edit.html", {"form": form})