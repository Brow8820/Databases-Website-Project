from telnetlib import STATUS
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

STATES = [
    ('ALABAMA','AL'),
    ('ALASKA','AK'),
    ('ARIZONA','AZ'),
    ( 'ARKANSAS','AR'),
    ('CALIFORNIA','CA'),
    ('Colorado','CO'),
    ('Connecticut','CT'),
    ('Delaware','DE'),
    ('Florida','FL'),
    ('Georgia','GA'),
    ('Hawaii','HI'),
    ('Idaho','ID'),
    ('Illinois','IL'),
    ('Indiana','IN'),
    ('Iowa','IA'),
    ('Kansas','KS'),
    ('Kentucky', 'KY'),
    ('Louisiana', 'LA'),
    ('Maine', 'ME'),
    ('Maryland', 'MD'),
    ('Massachusetts', 'MA'),
    ('Michigan', 'MI'),
    ('Minnesota', 'MN'),
    ('Mississippi', 'MS'),
    ('Missouri', 'MO'),
    ('Montana', 'MT'),
    ('Nebraska', 'NE'),
    ('Nevada', 'NV'),
    ('New Hampshire', 'NH'),
    ('New Jersey', 'NJ'),
    ('New Mexico', 'NM'),
    ('New York', 'NY'),
    ('North Carolina', 'NC'),
    ('North Dakota', 'ND'),
    ('Ohio', 'OH'),
    ('Oklahoma', 'OK'),
    ('Oregon', 'OR'),
    ('Pennsylvania', 'PA'),
    ('Rhode Island', 'RI'),
    ('South Carolina', 'SC'),
    ('South Dakota', 'SD'),
    ('Tennessee', 'TN'),
    ('Texas', 'TX'),
    ('Utah', 'UT'),
    ('Vermont', 'VT'),
    ('Virgin Islands', 'VI'),
    ('Virginia', 'VA'),
    ('Washington', 'WA'),
    ('West Virginia', 'WV'),
    ('Wisconsin', 'WI'),
    ('Wyoming', 'WY')
]
class Address(models.Model):
   
    StreetAddr = models.CharField(max_length = 512, null = False)
    City = models.CharField(max_length = 512, null = False)
    #State = models.CharField(max_length = 2, choices = STATES, null = False)
    Zip = models.IntegerField()

class Customer(models.Model):
    FirstName = models.CharField(max_length=99, help_text='', null = False)
    LastName = models.CharField(max_length=99, help_text='', null = False)
    Email = models.EmailField(max_length=256, null = False)
    StreetAddr = models.CharField(max_length = 512, null = False)
    City = models.CharField(max_length = 512, null = False)
    State = models.CharField(max_length = 14, choices = STATES, null = False)
    Zip = models.IntegerField()
    Phone = models.IntegerField( null = True)
    def __str__(self):
        return self.FirstName
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class Order(models.Model):
    Status = models.CharField(max_length=99, null = False)
    OrderNumber = models.IntegerField(null = False)
    TrackingNumber = models.IntegerField(null = False)
    #ShippingAddress = models.ManyToManyField(Address)        
    def __str__(self):
        return self.OrderNumber
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class PaymentMethod(models.Model):
    CardNumber = models.IntegerField(null = False)
    CardCompany = models.CharField(max_length=99, null = False)
    NameOnCard = models.CharField(max_length=99, null = False)
    Expiration = models.IntegerField(null = False)
    CVV = models.IntegerField(null = False)
    CardType = models.CharField(max_length=99, null = False)
    #BillingAddress = models.ManyToManyField(Address)
    def __str__(self):
        return self.NameOnCard
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class Product(models.Model):
    ProductName = models.CharField(max_length=99, null = False)
    #Inventory as a integer for count?
    Inventory = models.IntegerField(null = False)
    # file will be uploaded to MEDIA_ROOT / uploads                (either FileField or ImageField should be used)
    Picture = models.ImageField(upload_to = 'uploads/', null = True) 
    Type = models.CharField(max_length=99, null = False)
    Price = models.IntegerField(null = False)
    Rating  = models.IntegerField(null = False) # 1-5 rating?
    ProductID = models.IntegerField(null = False)
    ShippingCost = models.IntegerField(null = False)
    def __str__(self):
        return self.ProductName
    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

class Company(models.Model):
    CompanyName = models.CharField(max_length=99, null = False)
    SupportEmail = models.EmailField(max_length=256, null = False)
    SupportPhone = models.IntegerField( null = True)
    StreetAddr = models.CharField(max_length = 512, null = False)
    City = models.CharField(max_length = 512, null = False)
    State = models.CharField(max_length = 14, choices = STATES, null = False)
    Zip = models.IntegerField()
    CompanyID =  models.IntegerField(null = False)
    AboutUs = models.CharField(max_length=512, null = False)
    def __str__(self):
        return self.CompanyName
    def get_absolute_url(self):
        return reverse('company-detail', args=[str(self.id)])

class WishList(models.Model):
    test = models.IntegerField(null = False)
    user = models.ForeignKey(User, related_name = "wishList", on_delete = models.CASCADE)
    items = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="wlistItem")
    slug = models.SlugField(max_length=160, db_index=True)

    def __str__(self):
        return self.items.ProductName
    def get_absolute_url(self):
        return reverse("Wish_detail", args=[self.slug])
    