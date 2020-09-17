from django.db import models

# Create your models here.

class Target(models.Model):
    hash_code = models.CharField(max_length=20)
    target = models.CharField(max_length=200)
    def __str__ (self):
        return self.hash_code 
    def target_from_obj(self , obj):
        return obj.target




