from django.shortcuts import render
from .models import Customer, Order, PaymentMethod, Company, Product

def index(request):
    num_products = Product.objects.all().count()
    num_companies = Company.objects.all().count()

    context = {
        'num_products' : num_products,
        'num_companies' : num_companies,
    }

    return render(request,'index.html', context=context)
