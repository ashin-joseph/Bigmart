from django.db import models

class addcategoryDb(models.Model):
    ac_name=models.CharField(max_length=50,null=True,blank=True)
    ac_description=models.CharField(max_length=100,null=True,blank=True)
    ac_image=models.ImageField(upload_to="ac_pic",null=True,blank=True)
class productDb(models.Model):
    p_category=models.CharField(max_length=50,null=True,blank=True)
    p_name=models.CharField(max_length=50,null=True,blank=True)
    p_price=models.IntegerField(null=True,blank=True)
    p_description=models.CharField(max_length=100,null=True,blank=True)
    p_image=models.ImageField(upload_to="prd_pic",null=True,blank=True)
