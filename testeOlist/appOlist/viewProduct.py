from django.shortcuts import render, redirect
from appOlist.forms import ProductForm
from appOlist.models import Products

# Create your views here.
def indexProduct(request):
    data = {}
    data['db'] = Products.objects.all()
    return render(request, 'indexProduct.html', data)

def formProduct(request):
    data = {}
    data['formProduct'] = ProductForm()
    return render(request, 'formProduct.html', data)

def createProduct(request):
    formProduct = ProductForm(request.POST or None)
    if formProduct.is_valid():
        formProduct.save()
        return redirect('indexProduct')

def viewProduct(request, pk):
    data = {}
    data['db'] = Products.objects.get(pk=pk)
    return render(request, 'viewProduct.html', data)

def editProduct(request, pk):
    data = {}
    data['db'] = Products.objects.get(pk=pk)
    data['formProduct'] = ProductForm(instance=data['db'])
    return render(request, 'formProduct.html', data)

def updateProduct(request, pk):
    data = {}
    data['db'] = Products.objects.get(pk=pk)
    formProduct = ProductForm(request.POST or None, instance=data['db'])
    if formProduct.is_valid():
        formProduct.save()
        return redirect('indexProduct')

def deleteProduct(request, pk):
    db = Products.objects.get(pk=pk)
    db.delete()
    return redirect('indexProduct')