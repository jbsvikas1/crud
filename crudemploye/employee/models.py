from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField(unique=True)  
    econtact = models.CharField(max_length=15)

    def __str__(self):
        return self.ename
