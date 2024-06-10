from django.db import models

class contactDb(models.Model):
    contact_name=models.CharField(max_length=50,null=True,blank=True)
    contact_email=models.EmailField(max_length=50,null=True,blank=True)
    contact_number=models.IntegerField(null=True,blank=True)
    contact_subject=models.CharField(max_length=50,null=True,blank=True)
    contact_message=models.CharField(max_length=200,null=True,blank=True)
class Reg_signUp(models.Model):
    su_username=models.CharField(max_length=50, null=True, blank=True)
    su_password=models.CharField(max_length=100, null=True, blank=True)
    su_conformpassword=models.CharField(max_length=100, null=True,blank=True)
    su_email=models.EmailField(max_length=100, null=True, blank=True)
    su_pic=models.ImageField(upload_to="signup_Profilepic",null=True,blank=True)
class cartDb(models.Model):
    cart_username=models.CharField(max_length=50,null=True,blank=True)
    cart_productname=models.CharField(max_length=50,null=True,blank=True)
    cart_quantity=models.IntegerField(null=True,blank=True)
    cart_price=models.IntegerField(null=True,blank=True)
class checkoutDb(models.Model):
    checkout_username=models.CharField(max_length=50, null=True,blank=True)
    checkout_email=models.EmailField(max_length=50, null=True,blank=True)
    checkout_place=models.CharField(max_length=50, null=True,blank=True)
    checkout_address=models.TextField(null=True,blank=True)
    checkout_Phone=models.IntegerField(null=True,blank=True)
    checkout_message=models.TextField(null=True,blank=True)
    checkout_overall_total=models.IntegerField(null=True,blank=True)