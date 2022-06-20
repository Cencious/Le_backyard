from django.db import models

# Create your models here.

#location model
class location(models.Model):
    name= models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_location(self):
        self.save()
    
    def __str__(self):
        return self.name


