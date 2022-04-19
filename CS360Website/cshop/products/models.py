from telnetlib import STATUS
from django.db import models

# Create your models here.


class Address(models.Model):
    STATES = [
        ('AL', 'ALABAMA'),
        ('AK', 'ALASKA'),
        ('AZ','ARIZONA'),
        ('AR', 'ARKANSAS'),
        ('CA', 'CALIFORNIA'),
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
        ('Kentucky KY'),
        ('Louisiana LA'),
        ('Maine ME'),
        ('Maryland MD'),
        ('Massachusetts MA'),
        ('Michigan MI'),
        ('Minnesota MN'),
        ('Mississippi MS'),
        ('Missouri MO'),
        ('Montana MT'),
        ('Nebraska NE'),
        ('Nevada NV'),
        ('New Hampshire NH'),
        ('New Jersey NJ'),
        ('New Mexico NM'),
        ('New York NY'),
        ('North Carolina NC'),
        ('North Dakota ND'),
        ('Ohio OH'),
        ('Oklahoma OK'),
        ('Oregon OR'),
        ('Pennsylvania PA'),
        ('Rhode Island RI'),
        ('South Carolina SC'),
        ('South Dakota SD'),
        ('Tennessee TN'),
        ('Texas TX'),
        ('Utah UT'),
        ('Vermont VT'),
        ('Virgin Islands VI'),
        ('Virginia VA'),
        ('Washington WA'),
        ('West Virginia WV'),
        ('Wisconsin WI'),
        ('Wyoming	WY')
    ]
    StreetAddr = models.CharField(max_length = 512, null = False)
    City = models.CharField(max_length = 512, null = False)
    State = models.CharField(max_length = 2, choices = STATES, null = False)
    Zip = models.IntegerField()

class Customer(models.Model):
    FirstName = models.CharField(max_length=99, help_text='', null = False)
    LastName = models.CharField(max_length=99, help_text='', null = False)
    Email = models.EmailField(max_length=256, null = False)
    Address = models.ManyToManyField(Address)
    Phone = models.IntegerField(max_length=10, null = True)
    def __str__(self):
        return self.field_name
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class Orders(models.Model):
    Status = models.CharField(max_length=99, null = False)
    OrderNumber = models.IntegerField(max_length=50, null = False)
    TrackingNumber = models.IntegerField(max_length=50, null = False)
    ShippingAddress = models.ManyToManyField(Address)        
    def __str__(self):
        return self.field_name
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class PaymentMethod(models.Model):
    CardNumber = models.IntegerField(max_length=16, null = False)
    CardCompany = models.CharField(max_length=99, null = False)
    NameOnCard = models.CharField(max_length=99, null = False)
    Expiration = models.IntegerField(max_length=6, null = False)
    CVV = models.IntegerField(max_length=3, null = False)
    CardType = models.CharField(max_length=99, null = False)
    BillingAddress = models.ManyToManyField(Address)
    def __str__(self):
        return self.field_name
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class Product(models.Model):
    ProductName = models.CharField(max_length=99, null = False)
    #Inventory as a integer for count?
    Inventory = models.IntegerField(max_length=99, null = False)
    # file will be uploaded to MEDIA_ROOT / uploads                (either FileField or ImageField should be used)
    Picture = models.ImageField(upload_to = 'uploads/') 
    Type = models.CharField(max_length=99, null = False)
    Price = models.IntegerField(max_length=10, null = False)
    Rating  = models.IntegerField(max_length=5, null = False) # 1-5 rating?
    ProductID = models.IntegerField(max_length=99, null = False)
    ShippingCost = models.IntegerField(max_length=10, null = False)
    def __str__(self):
        return self.field_name
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class Company(models.Model):
    CompanyName = models.CharField(max_length=99, null = False)
    SupportEmail = models.EmailField(max_length=256, null = False)
    SupportPhone = models.IntegerField(max_length=10, null = True)
    CompanyAddress = models.ManyToManyField(Address)
    CompanyID =  models.IntegerField(max_length=10, null = False)
    AboutUs = models.CharField(max_length=512, null = False)
    def __str__(self):
        return self.field_name
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])