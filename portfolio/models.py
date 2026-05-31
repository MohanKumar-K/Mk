from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100, default="Mohan Kumar")
    role = models.CharField(max_length=100, default="Full Stack Developer")
    hero_description = models.TextField()
    about_description = models.TextField()
    resume_link = models.URLField(blank=True, null=True, help_text="Link for downloading resume")
    resume_view_link = models.URLField(blank=True, null=True, help_text="Link for viewing resume in browser")
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Interest(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class, e.g., 'fas fa-code'")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, help_text="e.g., 'fas fa-palette'")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    code_snippet = models.TextField(default="print('Hello World')", help_text="Small code snippet for the flip card back")
    icon = models.CharField(max_length=10, help_text="Emoji or short text icon, e.g., '🌐'")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category__order', 'order']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="e.g., 'fas fa-car'")
    github_link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class TechBadge(models.Model):
    project = models.ForeignKey(Project, related_name='tech_badges', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=100, help_text="e.g., Bachelor of Engineering")
    specialization = models.CharField(max_length=100, help_text="e.g., Electronics and Communication Engineering")
    institution = models.CharField(max_length=200, help_text="e.g., Velammal Engineering College")
    year_range = models.CharField(max_length=50, help_text="e.g., 2021 - 2025")
    score_type = models.CharField(max_length=50, help_text="e.g., CGPA or Percentage")
    score_value = models.CharField(max_length=50, help_text="e.g., 8.30 or 91.14%")
    icon_class = models.CharField(max_length=50, help_text="e.g., 'fas fa-graduation-cap'")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class Experience(models.Model):
    job_title = models.CharField(max_length=150, help_text="e.g., Software Engineer")
    company = models.CharField(max_length=200, help_text="e.g., Google")
    duration = models.CharField(max_length=100, help_text="e.g., Jun 2023 – Present")
    description = models.TextField(help_text="Describe your responsibilities and achievements")
    icon_class = models.CharField(max_length=50, default="fas fa-briefcase", help_text="e.g., 'fas fa-briefcase'")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.email}"

    class Meta:
        ordering = ['-created_at']
