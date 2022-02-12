from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model

# Create your models here.
STATE_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('Dhaka Metro', 'Dhaka Metro'),
    ('Dhaka Mirpur 10', 'Dhaka Mirpur 10'),
    ('Dhaka Gulshan', 'Dhaka Gulshan'),
    ('Dhaka Mirpur 12', 'Dhaka Mirpur 12'),
    ('Sylhet', 'Sylhet'),
    ('Kanaigat', 'Kanaigat'),
    ('Beanibazar', 'Beanibazar'),
    ('Golapgonj', 'Golapgonj'),
    ('Jkoigonj', 'Joigonj'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('C', 'Covid 19 Special'),
    ('D', 'Devices'),
    ('H', 'Herbal and Homeopathy'),
    ('BM', 'Baby & Mom care'),
    ('ND', 'Nutrition and drinks'),
    ('PC', 'Personal care'),
    ('OM', 'OTC Medicines'),
    ('PM', 'Prescription Medicines'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="Pending")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
