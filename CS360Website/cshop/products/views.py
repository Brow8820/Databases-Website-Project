from django.shortcuts import render,redirect
from .models import WishList,Customer, Order, PaymentMethod, Company, Product
from django.views import generic
from django.contrib.auth import login
from django.contrib import messages


def index(request):
    num_products = Product.objects.all().count()
    num_companies = Company.objects.all().count()

    context = {
        'num_products' : num_products,
        'num_companies' : num_companies,
    }

    return render(request,'index.html', context=context)

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Product.objects.all().filter(ProductName=search)
        post |= Product.objects.all().filter(ProductName__contains=search)
        return render(request, 'searchbar.html', {'post':post})

class ProductListView(generic.ListView):
    model = Product
    context_object_name= 'product_list'
    paginate_by = 15

class ProductDetailView(generic.DetailView):
    model = Product
    def addWish(cust, prod):
        try:    
            b = WishList(user=cust, item = prod)
            b.save()
        except:
            return("Could Not Add Item")

class CompanyListView(generic.ListView):
    model = Company
    context_object_name= 'companies_list'  
    paginate_by = 15  

class CompanyDetailView(generic.DetailView):
    model = Company

class Product100(generic.ListView):
    model = Product
    filtered = Product.objects.all().filter(Price__lte=100)
    context_object_name = 'product_100'
    paginate_by = 15

class ProductDetailView100(generic.DetailView):
    model = Product