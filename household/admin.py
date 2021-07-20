from django.contrib import admin
from .models import Family, Membership

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    list_display = ['name']
