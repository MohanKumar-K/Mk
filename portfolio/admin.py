from django.contrib import admin
from .models import Contact, PersonalInfo, Interest, SkillCategory, Skill, Project, TechBadge, Education, Experience

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'order')
    list_editable = ('order',)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'order')
    list_editable = ('order',)
    inlines = [SkillInline]

class TechBadgeInline(admin.TabularInline):
    model = TechBadge
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'order')
    list_editable = ('order',)
    inlines = [TechBadgeInline]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'duration', 'order')
    list_editable = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year_range', 'order')
    list_editable = ('order',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
