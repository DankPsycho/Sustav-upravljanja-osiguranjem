from django.db import models



class Category(models.Model):
    category_name = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now=True)    
    def __str__(self):
        return f" {self.category_name}"
    class Meta:
        verbose_name_plural = "Categories"


class Policy(models.Model):
    category= models.OneToOneField(Category, on_delete=models.CASCADE)  # <---- One to one
    policy_name=models.CharField(max_length=200)
    sum_assurance=models.PositiveIntegerField()
    premium=models.PositiveIntegerField()
    tenure=models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return f" {self.policy_name}"
    class Meta:
        verbose_name_plural = "Policies"

class Customer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    policy = models.ManyToManyField(Policy)                             # <---- Many to many
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Customers"
    def __str__(self):
        return f"{self.name}"

class PolicyRecord(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)     # <---- One to Many / Many to one
    Policy= models.ForeignKey(Policy, on_delete=models.CASCADE)         # <---- One to Many / Many to one
    status = models.CharField(max_length=20,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return f" {self.Policy}"
    class Meta:
        verbose_name_plural = "PolicyRecords"