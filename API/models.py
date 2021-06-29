from django.db import models

# Create your models here.



class Customer(models.Model):
   first_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)
   email = models.EmailField()
   tel = models.CharField(max_length= 11)
   content = models.TextField()
   created_date =models.DateTimeField(auto_now_add = True)
   def __str__(self):
        return self.first_name 
        