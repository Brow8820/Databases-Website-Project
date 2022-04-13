from django.db import models

# Create your models here.


class Address(models.Model):
    STATES = [
        ('AL', 'ALABAMA'),
        ('AK', 'ALASKA'),
        ('AZ','ARIZONA'),
        ('AR', 'ARKANSAS'),
        ('CA', 'CALIFORNIA'),

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
