from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#location model
class Location(models.Model):
    name= models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_location(self):
        self.save()
    
    def __str__(self):
        return self.name
class NeighbourHood(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    police_cont=models.IntegerField(null=True,blank=True)
    hospital_cont=models.IntegerField(null=True,blank=True)
    photo=CloudinaryField(blank=True,) 

    def create_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def search_by_name(cls,search_term):
        hood =cls.objects.filter(name__icontains=search_term)

    @classmethod
    def find_neighborhood(cls,id):
        hood =cls.objects.get(id=id)
        return hood

    def __str__(self):
        return "%s neighborhood" % self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = CloudinaryField('image')

    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    joined_on=models.DateTimeField(auto_now=True)


    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    def __str__(self):
        return str(self.user)

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile       
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
   
# business class model
class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)

    # create business
    def create_business(self):
        self.save()

    # delete business
    def delete_business(self):
        self.delete()

    # update business
    def update_business(self):
        self.update()
    
    def __str__(self):
        return self.name
class Post(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
   

    # create post
    def create_post(self):
        self.save()

    # delete post
    def delete_post(self):
        self.delete()

    # update post
    def update_post(self):
        self.update()