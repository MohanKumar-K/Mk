# Developer Portfolio - Django Project

A dynamic, fully-featured personal portfolio website built with Django. This project showcases personal information, skills, projects, education, experience, and includes a contact form.

## 🚀 Features & Content Specification

This portfolio is entirely database-driven, meaning all content can be managed via the Django Admin panel without touching the code. The content is structured into the following models:

- **Personal Info:** Manage your name, role, hero description, about section, resume links, and social links (GitHub, LinkedIn, Email).
- **Interests:** List your personal interests or hobbies with FontAwesome icons.
- **Skills:** 
  - Organized by **Skill Categories** (e.g., Frontend, Backend, Tools).
  - Individual **Skills** feature flip-cards with short code snippets on the back.
- **Projects:** Showcase your work with a title, description, GitHub link, and associated **Tech Badges** to highlight the stack used.
- **Education:** Timeline of your educational background including degrees, institutions, duration, and scores (CGPA/Percentage).
- **Experience:** Timeline of your professional experience including job titles, companies, duration, and responsibilities.
- **Contact:** A built-in contact form that saves messages directly to the database for easy viewing in the admin panel.

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default for development)
- **Environment Management:** python-decouple
- **Frontend:** HTML, CSS (Vanilla/Custom), FontAwesome (for icons)

## ⚙️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd mk
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory (where `manage.py` is located) and add your configurations:
   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for the Admin Panel:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Populate Database (Optional):**
   If you want some dummy data to start with, run the provided script:
   ```bash
   python populate_db.py
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000` in your browser. Access the admin panel at `http://127.0.0.1:8000/admin`.

## 📁 Project Structure

```
d:\mk\
├── .env                # Environment variables (ignored in git)
├── .gitignore          # Git ignore rules
├── db.sqlite3          # SQLite database (ignored in git)
├── manage.py           # Django management script
├── populate_db.py      # Script to populate initial database records
├── requirements.txt    # Python dependencies
├── venv/               # Virtual environment (ignored in git)
├── portfolio/          # Main Django app containing views, models, templates, etc.
└── devportfolio/       # Django project configuration (settings, urls)
```
