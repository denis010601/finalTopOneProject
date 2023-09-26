from django.contrib import admin
from .models import UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name')
    search_fields = ('user__username', 'first_name', 'last_name')
