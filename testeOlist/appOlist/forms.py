from django.forms import ModelForm
from appOlist.models import Sellers, Products, Marketplaces, Categories

# Create the form class.
class SellerForm(ModelForm):
    class Meta:
        model = Sellers
        fields = ['name', 'socialReason', 'cnpj', 'email', 'phone', 'address']

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'value', 'category']

class MarketplaceForm(ModelForm):
    class Meta:
        model = Marketplaces
        fields = ['name', 'socialReason', 'site', 'email', 'phone', 'address']

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']
