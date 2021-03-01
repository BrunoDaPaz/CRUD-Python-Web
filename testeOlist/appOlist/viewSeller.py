from django.shortcuts import render, redirect
from django.http import HttpResponse
from appOlist.forms import SellerForm
from appOlist.models import Sellers

# Create your views here.
def indexSeller(request):
    data = {}
    data['db'] = Sellers.objects.all()
    return render(request, 'indexSeller.html', data)

def formSeller(request):
    data = {}
    data['formSeller'] = SellerForm()
    return render(request, 'formSeller.html', data)

def createSeller(request):
    formSeller = SellerForm(request.POST or None)
    if formSeller.is_valid():
        formSeller.save()
        return redirect('indexSeller')

def viewSeller(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    return render(request, 'viewSeller.html', data)

def editSeller(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    data['formSeller'] = SellerForm(instance=data['db'])
    return render(request, 'formSeller.html', data)

def updateSeller(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    formSeller = SellerForm(request.POST or None, instance=data['db'])
    if formSeller.is_valid():
        formSeller.save()
        return redirect('indexSeller')

def deleteSeller(request, pk):
    db = Sellers.objects.get(pk=pk)
    db.delete()
    return redirect('indexSeller')