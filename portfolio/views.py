from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Project, Skill, Experience, Profile

def home(request):
    """Homepage with hero section and overview"""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()[:8]
    recent_experience = Experience.objects.first()
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills': skills,
        'recent_experience': recent_experience,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """About page with detailed info"""
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'portfolio/about.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 9

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

def contact(request):
    """Contact page"""
    profile = Profile.objects.first()
    return render(request, 'portfolio/contact.html', {'profile': profile})

# API endpoint for dynamic content
def skills_api(request):
    """API endpoint to return skills data for animations"""
    skills = list(Skill.objects.values('name', 'level', 'icon', 'category'))
    return JsonResponse({'skills': skills})
