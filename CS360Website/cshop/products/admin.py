from django.contrib import admin
from .models import Customer, Order, PaymentMethod, Company, Product
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(PaymentMethod)
admin.site.register(Company)
admin.site.register(Product)


