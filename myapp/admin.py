from django.contrib import admin
from .models import Database, Profile, contact
admin.site.register(Database)
admin.site.register(contact)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'age', 'profile_image', 'registration_date']

# Register your models here.
