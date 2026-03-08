from django.shortcuts import render
from django.contrib import messages
from .models import Contact, PersonalInfo, Interest, SkillCategory, Project, Education, Experience


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all fields.')

    # Fetch dynamic data
    personal_info = PersonalInfo.objects.first()
    interests = Interest.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.prefetch_related('tech_badges').all()
    experience_entries = Experience.objects.all()
    education_entries = Education.objects.all()

    context = {
        'personal_info': personal_info,
        'interests': interests,
        'skill_categories': skill_categories,
        'projects': projects,
        'experience_entries': experience_entries,
        'education_entries': education_entries,
    }

    return render(request, 'portfolio/index.html', context)
