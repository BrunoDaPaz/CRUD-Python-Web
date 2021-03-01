from django.shortcuts import render, redirect
from django.http import HttpResponse
from appOlist.forms import CategoryForm
from appOlist.models import Categories

# Create your views here.
def home(request):
    data = {}
    data['db'] = Categories.objects.all()
    return render(request, 'index.html', data)

def indexCategory(request):
    data = {}
    data['db'] = Categories.objects.all()
    return render(request, 'indexCategory.html', data)

def form(request):
    data = {}
    data['form'] = CategoryForm()
    return render(request, 'form.html', data)

def create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('indexCategory')

def view(request, pk):
    data = {}
    data['db'] = Categories.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Categories.objects.get(pk=pk)
    data['form'] = CategoryForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Categories.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('indexCategory')

def delete(request, pk):
    db = Categories.objects.get(pk=pk)
    db.delete()
    return redirect('indexCategory')