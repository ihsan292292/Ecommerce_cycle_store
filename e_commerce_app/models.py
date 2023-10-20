from django.db import models



# Create your models here.
class seller_register(models.Model):
    seller_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    company_name = models.CharField(max_length=50)
    company_details = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    photo = models.FileField(upload_to='e_commerce_app/static/profile_photos')
    
    def __str__(self):
        return self.seller_name

class add_product(models.Model):
    bike_choice=[
        ('Mountain Bikes','Mountain Bikes'),
        ('Electric Bicycles','Electric Bicycles'),
        ('Road Bikes','Road Bikes'),
        ('Hybrid Bikes','Hybrid Bikes'),
        ('Folding Bikes','Folding Bikes'),
        ('Comfort Bikes','Comfort Bikes')   
    ]
    age_choice=[
        ('three-five','three-five'),
        ('five-nine','five-nine'),
        ('nine-forteen','nine-forteen'),
        ('forteen-ninteen','forteen-ninteen'),
        ('ninteen-twentyfive','ninteen-twentyfive'),
        ('25_above','25_above')
    ]
    speed_choice=[
        ('one','one'),
        ('two','two'),
        ('three','three'),
        ('four','four'),
        ('five','five'),
        ('six','six')
    ]
    bike_type = models.CharField(max_length=50,choices=bike_choice)
    age_range = models.CharField(max_length=50,choices=age_choice)
    brand = models.CharField(max_length=50)
    noOfSpeed = models.CharField(max_length=50,choices=speed_choice)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    file_image = models.FileField(upload_to='e_commerce_app/static/Uploaded_images')
    
    def __str__(self):
        return self.brand
    
class buyer_register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class wishlist(models.Model):
    user_id = models.IntegerField()
    prod_id = models.IntegerField()
    bike_type = models.CharField(max_length=50)
    age_range = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    noOfSpeed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    file_image = models.FileField()
    
    def __str__(self):
        return self.brand
    
class cart(models.Model):
    user_id = models.IntegerField()
    prod_id = models.IntegerField()
    quantity = models.IntegerField()
    bike_type = models.CharField(max_length=50)
    age_range = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    noOfSpeed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    file_image = models.FileField()
    
    def __str__(self):
        return self.brand
    
class delivary_details(models.Model):
    uname = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    user_id = models.IntegerField()
    order_date = models.DateField(auto_now_add=True,null=True)
    estimated_delivery = models.DateField(null=True,)
    products = models.TextField()
    products_image = models.CharField(max_length=50)
    total_amount_paid = models.IntegerField()
    
    def __str__(self):
        return self.uname
    
