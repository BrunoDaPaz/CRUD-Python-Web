from django.contrib import admin
from django.urls import path
from appOlist.viewSeller import indexSeller, formSeller, createSeller, viewSeller, editSeller, updateSeller, deleteSeller
from appOlist.viewProduct import indexProduct, formProduct, createProduct, viewProduct, editProduct, updateProduct, deleteProduct
from appOlist.viewMarketplace import indexMarketplace, formMarketplace, createMarketplace, viewMarketplace, editMarketplace, updateMarketplace, deleteMarketplace
from appOlist.views import home, indexCategory, form, create, view, edit, update, delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('indexCategory/', indexCategory, name="indexCategory"),
    path('form/', form, name="form"),
    path('create/', create, name="create"),
    path('view/<int:pk>/', view, name="view"),
    path('edit/<int:pk>/', edit, name="edit"),
    path('update/<int:pk>/', update, name="update"),
    path('delete/<int:pk>/', delete, name="delete"),

    path('indexSeller/', indexSeller, name="indexSeller"),
    path('formSeller/', formSeller, name="formSeller"),
    path('createSeller/', createSeller, name="createSeller"),
    path('viewSeller/<int:pk>/', viewSeller, name="viewSeller"),
    path('editSeller/<int:pk>/', editSeller, name="editSeller"),
    path('updateSeller/<int:pk>/', updateSeller, name="updateSeller"),
    path('deleteSeller/<int:pk>/', deleteSeller, name="deleteSeller"),

    path('indexProduct/', indexProduct, name="indexProduct"),
    path('formProduct/', formProduct, name="formProduct"),
    path('createProduct/', createProduct, name="createProduct"),
    path('viewProduct/<int:pk>/', viewProduct, name="viewProduct"),
    path('editProduct/<int:pk>/', editProduct, name="editProduct"),
    path('updateProduct/<int:pk>/', updateProduct, name="updateProduct"),
    path('deleteProduct/<int:pk>/', deleteProduct, name="deleteProduct"),

    path('indexMarketplace/', indexMarketplace, name="indexMarketplace"),
    path('formMarketplace/', formMarketplace, name="formMarketplace"),
    path('createMarketplace/', createMarketplace, name="createMarketplace"),
    path('viewMarketplace/<int:pk>/', viewMarketplace, name="viewMarketplace"),
    path('editMarketplace/<int:pk>/', editMarketplace, name="editMarketplace"),
    path('updateMarketplace/<int:pk>/', updateMarketplace, name="updateMarketplace"),
    path('deleteMarketplace/<int:pk>/', deleteMarketplace, name="deleteMarketplace"),
]