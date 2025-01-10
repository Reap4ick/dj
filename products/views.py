import os
from django.http import HttpResponse
from django.shortcuts import redirect, render

from products.forms.create import CreateProduct
from products.forms.edit import EditProduct
from products.models import Product
from django.core.files.storage import default_storage




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
        return render(request, "detail.html", {"product": product,"return_url": "/products/list"})
    except:
        error="Product not except"
        return render(request, "detail.html", {"error": error,"return_url": "/products/list"})
    
    # return render(request, "detail.html", {"product": product, "error": error})

def moredetail(request, id):
    try:
        product = Product.objects.get(pk=id)
        print(product)
        return render(request, "moredetail.html", {"product": product,"return_url": "/products/catalog"})
    except:
        error="Product not except"
        return render(request, "moredetail.html", {"error": error,"return_url": "/products/catalog"})


def delete(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

    if product.photo:
        default_storage.delete(product.photo.name)
    
    product.delete()
    
    return redirect("/products/home")



def create(request):

    form = CreateProduct()

    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/products/list")

    return render(request, "create.html", {"form": form,"return_url": "/products/list"})

def catalog(request):
    products = Product.objects.all()
    return render(request, "catalog.html", {"products": products})

def edit(request, id):

    product = Product.objects.get(id=id)

    if product is None:
        return HttpResponse("User not found")

    form = EditProduct(instance=product)

    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect("/products/list")

    return render(request, "edit.html", {"form": form,"return_url": "/products/list"})