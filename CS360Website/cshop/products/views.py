from django.shortcuts import render
from .models import Customer, Order, PaymentMethod, Company, Product
from django.views import generic

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
        post = Product.objects.all().filter(title=search)
        return render(request, 'searchbar.html', {'post':post})

class ProductListView(generic.ListView):
    model = Product
    context_object_name= 'product_list'
    paginate_by = 15

class ProductDetailView(generic.DetailView):
    model = Product

class CompanyListView(generic.ListView):
    model = Company
    context_object_name= 'companies_list'  
    paginate_by = 15  

class CompanyDetailView(generic.DetailView):
    model = Company
