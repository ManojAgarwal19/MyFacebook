from django.contrib import admin
from psutil import users
from social.models import UserProfile,UserPost

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserPost)