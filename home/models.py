from django.db import models

# Create your models here.
class message(models.Model):
    email=models.EmailField(max_length=254)
    text_field=models.TextField(blank=True, null=True,max_length=10000)
    def __str__(self):
        return self.email
    