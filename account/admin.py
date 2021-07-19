from django.contrib import admin
from .models import Profile, Family, Membership

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    list_display = ['user', 'date_of_birth']

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    list_display = ['name']
