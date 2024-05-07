from django.db import models

# Create your models here.
class JobDescription(models.Model):
    name = models.CharField(max_length=100,null=True)
    details = models.CharField(max_length=100,null=True)
    
class Designation(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    
class Department(models.Model):
    name = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    
    
class Employee(models.Model):
    name = models.CharField(max_length=100,null=True)
    fname = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    dateofjoining =models.DateField(max_length=100 ,null=True)
    designation = models.CharField(max_length=100,null =True)
    jobdecription = models.CharField(max_length=100,null =True)

    jobdecription = models.ForeignKey(JobDescription,on_delete=models.CASCADE,null=True) 
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,null=True)   
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    
class Location(models.Model):
    name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    

    

