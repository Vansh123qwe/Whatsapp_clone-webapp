from django.db import models

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=100)
     content=models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name

# Create your models here.

class frd(models.Model):
     friend=models.CharField(max_length=30)
     who=models.CharField(max_length=30)


     def __str__(self):
          return self.who

class massage(models.Model):
     who=models.CharField(max_length=30)
     body=models.TextField()
     whom=models.CharField(max_length=30)
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)




          