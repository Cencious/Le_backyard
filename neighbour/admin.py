from django.contrib import admin
from .models import Profile,Location,NeighbourHood,Post,Business


# Register your models here.
admin.site.register(Location)
admin.site.register(Business)
admin.site.register(Profile)

admin.site.register(NeighbourHood)
admin.site.register(Post)