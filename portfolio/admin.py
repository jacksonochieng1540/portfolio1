from django.contrib import admin
from .models import Profile, Project, Skill, Experience

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url', 'twitter_url', 'website_url')
        }),
        ('Resume', {
            'fields': ('resume',)
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('level',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_date')
    list_filter = ('featured', 'created_date', 'technologies')
    search_fields = ('title', 'description')
    list_editable = ('featured',)
    filter_horizontal = ('technologies',)
    date_hierarchy = 'created_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description', 'image')
        }),
        ('Technologies & Links', {
            'fields': ('technologies', 'github_url', 'live_url')
        }),
        ('Settings', {
            'fields': ('featured',)
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current')
    list_filter = ('current', 'start_date')
    search_fields = ('company', 'position')
    date_hierarchy = 'start_date'