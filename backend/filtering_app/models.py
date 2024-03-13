from django.db import models

# Create your models here.

class YelpData(models.Model):
    business_id =models.CharField(primary_key=True,max_length=150,unique=True, blank=False)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state =models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    stars = models.CharField(max_length=150)
    review_count = models.IntegerField()
    is_open = models.BooleanField(default=False)
    categories = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table = 'YelpData'
