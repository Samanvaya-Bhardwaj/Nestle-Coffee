# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# # Create your models here.

# CATEGORY_CHOICES = (
#     ('CF', 'Coffee'),
#     ('SNK', 'Snacks'),
#     ('SD', 'Soft Drinks'),
#     ('SHK', 'Shakes'),
# )

# SIZE_CHOICES = (
#     ('S', 'Small'),
#     ('M', 'Medium'),
#     ('L', 'Large'),
#     ('H', 'Half'),
#     ('F', 'Full'),
# )


# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
#     size = models.CharField(choices=SIZE_CHOICES, max_length=1, blank=True, null=True)
#     price = models.FloatField()
#     product_image = models.ImageField(upload_to='product')


#     def __str__(self):
#         return self.title



# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name, password=None):
#         user = self.create_user(email=email, name=name, password=password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.name


# nill

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
('Andaman & Nicobar Islands','Andaman & Nicobar Islands'), 
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'), 
('Assam','Assam'),
('Bihar','Bihar'), 
('Chandigarh','Chandigarh'), 
('Chattisgarh','Chattisgarh'),
('Dadra & Nagar Haveli','Dadra & Nagar Haveli'), 
('Daman and Diu','Daman and Diu'), 
('Delhi','Delhi'),
('Goa','Goa'),
('Gujrat','Gujrat'), 
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'), 
('Jammu & Kashmir','Jammu & Kashmir'), 
('Jharkhand','Jharkhand'), 
('Karnataka','Karnataka'), 
('Kerala','Kerala'), 
('Lakshadweep','Lakshadweep'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'), 
('Manipur','Manipur'), 
('Meghalaya','Meghalaya'), 
('Mizoram','Mizoram'), 
('Nagaland','Nagaland'), 
('Odisa','Odisa'), 
('Puducherry','Puducherry'), 
('Punjab','Punjab'), 
('Rajasthan','Rajasthan'), 
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'), 
('Telangana','Telangana'), 
('Tripura','Tripura'), 
('Uttarakhand','Uttarakhand'), 
('Uttar Pradesh','Uttar Pradesh'), 
('West Bengal','West Bengal'),
)

CATEGORY_CHOICES=(
    ('CF','Coffee'),
    ('SH','Shakes'),
    ('SN','Snacks'),
    ('SD','Softdrink'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)