from django.shortcuts import render,redirect
from .models import WishList,Customer, Order, PaymentMethod, Company, Product
from django.views import generic
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


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
    
    
def addwish(request, pk):
    x = int(pk)
    try:
        obj =  Product.objects.filter(pk=x).first()
    except:
        obj = None
    newOb = WishList(test = 1,user = request.user, items = obj)
    newOb.save()
    return HttpResponseRedirect('/products/product/'+str(pk))


class CompanyListView(generic.ListView):
    model = Company
    context_object_name= 'companies_list'  
    paginate_by = 15  

class CompanyDetailView(generic.DetailView):
    model = Company

class Product100(generic.ListView):
    model = Product
    context_object_name = 'product_100'
    paginate_by = 15
    def get_queryset(self):
        return Product.objects.all().filter(Price__lt =100)

class Product500(generic.ListView):
    model = Product
    context_object_name = 'product_500'
    paginate_by = 15
    def get_queryset(self):
        return Product.objects.all().filter(Price__range = [100,500])

class Product2000(generic.ListView):
    model = Product
    context_object_name = 'product_2000'
    paginate_by = 15
    def get_queryset(self):
        return Product.objects.all().filter(Price__range = [500,2000])

class Product5000(generic.ListView):
    model = Product
    context_object_name = 'product_5000'
    paginate_by = 15
    def get_queryset(self):
        return Product.objects.all().filter(Price__range = [2000,5000])

class Product5001(generic.ListView):
    model = Product
    context_object_name = 'product_5001'
    paginate_by = 15
    def get_queryset(self):
        return Product.objects.all().filter(Price__gte =5000)

class ProductwList(generic.ListView):
    model = Product
    context_object_name='product_wlist'
    paginate_by = 10
    def get_queryset(self):
        prodList = Product.objects.none()
        wlist = WishList.objects.all().filter(user = self.request.user)
        for query in wlist:
            prodList |= Product.objects.all().filter(pk = query.items.id)
        return prodList




class ProductDetailView100(generic.DetailView):
    model = Product

#push reset stuff