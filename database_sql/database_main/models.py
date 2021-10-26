from django.db import models

class mugisian(models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    instument= models.CharField(max_length=20)


    def __str__(self):
        return self.first_name

class album(models.Model):
    artist=models.ForeignKey(mugisian,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    Type=models.CharField(max_length=15)  

    
    def __str__(self):
        return self.name  
