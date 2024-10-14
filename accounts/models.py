from django.db import models
import re
# Create your models here.

class EducationProduct(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title
    
    def word_count(self):
        words  = re.findall(r'\w+', self.content)
        return len(words)
    

class PricingPost(models.Model):
    payment_plan = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

class StaffPost(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    subject = models.CharField(max_length=100)
    about = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
    
class NewsPost(models.Model):
    headline = models.CharField(max_length=300)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)  
    article = models.TextField()

class GalleryPost(models.Model):
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField()    
    message = models.TextField()

    def str(self):
        return self.first_name

