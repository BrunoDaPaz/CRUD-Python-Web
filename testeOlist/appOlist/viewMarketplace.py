from django.shortcuts import render, redirect
from appOlist.forms import MarketplaceForm
from appOlist.models import Marketplaces

# Create your views here.
def indexMarketplace(request):
    data = {}
    data['db'] = Marketplaces.objects.all()
    return render(request, 'indexMarketplace.html', data)

def formMarketplace(request):
    data = {}
    data['formMarketplace'] = MarketplaceForm()
    return render(request, 'formMarketplace.html', data)

def createMarketplace(request):
    formMarketplace = MarketplaceForm(request.POST or None)
    if formMarketplace.is_valid():
        formMarketplace.save()
        return redirect('indexMarketplace')

def viewMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    return render(request, 'viewMarketplace.html', data)

def editMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    data['formMarketplace'] = MarketplaceForm(instance=data['db'])
    return render(request, 'formMarketplace.html', data)

def updateMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    formMarketplace = MarketplaceForm(request.POST or None, instance=data['db'])
    if formMarketplace.is_valid():
        formMarketplace.save()
        return redirect('indexMarketplace')

def deleteMarketplace(request, pk):
    db = Marketplaces.objects.get(pk=pk)
    db.delete()
    return redirect('indexMarketplace')