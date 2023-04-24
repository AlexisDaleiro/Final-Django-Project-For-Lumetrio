from django.contrib import admin
from .models import Profile, Relationship
from django.contrib.admin import register as admin_register
from profiles.models import Profile
# Register your models here.

@admin_register
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'user', 'bio', 'email', 'country', 'avatar', 'friends']

admin.site.register(Profile)
admin.site.register(Relationship)