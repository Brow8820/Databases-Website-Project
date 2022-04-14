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
