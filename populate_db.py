import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devportfolio.settings')
django.setup()

from portfolio.models import Skill

snippets = {
    'HTML': '<section id="hero">\n  <h1>Mohan</h1>\n</section>',
    'CSS': '.hero {\n  backdrop-filter: blur(12px);\n}',
    'Bootstrap': '<div class="row g-4">\n  <div class="col-md-6">',
    'JavaScript': 'const init = () => {\n  gsap.to(".hero");\n}',
    'Python': 'def get_skills():\n  return Skill.all()',
    'Django': 'class Project(Model):\n  title = CharField()',
    'Java': 'public class Main {\n  public static void main(String[] args) { System.out.print("Java"); } }',
    'MySQL': 'SELECT title \nFROM projects LIMIT 5;',
    'IoT': 'temp = sensor.read()\nwifi.send(temp)',
    'Embedded Systems': 'void setup() {\n  pinMode(LED, 1);\n}',
    'Git': 'git commit -m "UI"\ngit push origin main'
}

for skill in Skill.objects.all():
    if skill.name in snippets:
        skill.code_snippet = snippets[skill.name]
        skill.save()
        print(f"Updated {skill.name}")
    else:
        skill.code_snippet = f"// {skill.name} init"
        skill.save()

print("Database population complete.")
