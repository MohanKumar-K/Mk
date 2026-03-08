import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devportfolio.settings')
django.setup()

from portfolio.models import PersonalInfo, Interest, SkillCategory, Skill, Project, TechBadge, Education

def populate():
    print("Clearing old data...")
    PersonalInfo.objects.all().delete()
    Interest.objects.all().delete()
    SkillCategory.objects.all().delete()
    Project.objects.all().delete()
    Education.objects.all().delete()

    print("Adding Personal Info...")
    PersonalInfo.objects.create(
        name="Mohan Kumar",
        role="Full Stack Developer",
        hero_description="I am a passionate Full Stack Developer with experience in Python, Django, Java, MySQL and modern web technologies. I enjoy building scalable web applications and intelligent systems. I also have interest in IoT and Embedded Systems.",
        about_description="I am a dedicated developer who loves turning ideas into reality through code. With a strong foundation in both frontend and backend technologies, I build robust, user-friendly applications. My curiosity extends beyond traditional software — I'm equally passionate about IoT systems and embedded programming, where software meets hardware to create innovative solutions.",
        resume_link="#"
    )

    print("Adding Interests...")
    interests = [
        ("Web Development", "fas fa-code", 1),
        ("Full Stack Development", "fas fa-layer-group", 2),
        ("IoT Systems", "fas fa-wifi", 3),
        ("Embedded Systems", "fas fa-microchip", 4),
        ("Software Engineering", "fas fa-cogs", 5)
    ]
    for title, icon, order in interests:
        Interest.objects.create(title=title, icon_class=icon, order=order)

    print("Adding Skills...")
    cat_front = SkillCategory.objects.create(name="Frontend", icon_class="fas fa-palette", order=1)
    Skill.objects.create(category=cat_front, name="HTML", icon="🌐", order=1)
    Skill.objects.create(category=cat_front, name="CSS", icon="🎨", order=2)
    Skill.objects.create(category=cat_front, name="Bootstrap", icon="📐", order=3)
    Skill.objects.create(category=cat_front, name="JavaScript", icon="⚡", order=4)

    cat_back = SkillCategory.objects.create(name="Backend", icon_class="fas fa-server", order=2)
    Skill.objects.create(category=cat_back, name="Python", icon="🐍", order=1)
    Skill.objects.create(category=cat_back, name="Django", icon="🚀", order=2)
    Skill.objects.create(category=cat_back, name="Java", icon="☕", order=3)

    cat_db = SkillCategory.objects.create(name="Database", icon_class="fas fa-database", order=3)
    Skill.objects.create(category=cat_db, name="MySQL", icon="🗄️", order=1)

    cat_other = SkillCategory.objects.create(name="Other Technologies", icon_class="fas fa-tools", order=4)
    Skill.objects.create(category=cat_other, name="IoT", icon="📡", order=1)
    Skill.objects.create(category=cat_other, name="Embedded Systems", icon="🔌", order=2)
    Skill.objects.create(category=cat_other, name="Git", icon="🔀", order=3)

    print("Adding Projects...")
    p1 = Project.objects.create(
        title="Smart Outdoor Car Protection Cover Using IoT",
        description="IoT based system to monitor and protect vehicles using sensors and real-time data communication.",
        icon_class="fas fa-car", order=1
    )
    for badge in ["IoT", "Sensors", "Embedded C", "Arduino"]:
        TechBadge.objects.create(project=p1, name=badge)

    p2 = Project.objects.create(
        title="GenZTech Mobile Service Website",
        description="Responsive website for mobile service booking with modern UI and seamless user experience.",
        icon_class="fas fa-mobile-alt", order=2
    )
    for badge in ["HTML", "CSS", "JavaScript", "Bootstrap"]:
        TechBadge.objects.create(project=p2, name=badge)

    p3 = Project.objects.create(
        title="Student Management System",
        description="Java application using MySQL to manage student records with CRUD operations and reporting.",
        icon_class="fas fa-user-graduate", order=3
    )
    for badge in ["Java", "MySQL", "JDBC"]:
        TechBadge.objects.create(project=p3, name=badge)

    p4 = Project.objects.create(
        title="Django Customer Response System",
        description="Web application to collect and store customer responses with an admin dashboard for management.",
        icon_class="fas fa-comments", order=4
    )
    for badge in ["Python", "Django", "SQLite", "Bootstrap"]:
        TechBadge.objects.create(project=p4, name=badge)

    print("Adding Education...")
    Education.objects.create(
        degree="Bachelor of Engineering",
        specialization="Electronics and Communication Engineering",
        institution="Velammal Engineering College",
        year_range="2021 – 2025",
        score_type="CGPA", score_value="8.30",
        icon_class="fas fa-graduation-cap", order=1
    )
    Education.objects.create(
        degree="XII Standard",
        specialization="Higher Secondary Education",
        institution="Holy Child Matriculation Higher Secondary School",
        year_range="2020 – 2021",
        score_type="Percentage", score_value="91.14%",
        icon_class="fas fa-school", order=2
    )
    Education.objects.create(
        degree="X Standard",
        specialization="Secondary Education",
        institution="Holy Child Matriculation Higher Secondary School",
        year_range="2018 – 2019",
        score_type="Percentage", score_value="91%",
        icon_class="fas fa-book-open", order=3
    )

    print("Done!")

if __name__ == '__main__':
    populate()
