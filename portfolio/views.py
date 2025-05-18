from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .models import Project
from .models import Education
from .models import Internship
from .models import Skill
from .models import Certification
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

def home(request):
    nav_items = [
        {"name": "Home", "url_name": "home"},
        {"name": "Education Details", "url_name": "education details"},
        {"name": "Internships", "url_name": "internships"},
        {"name": "Projects", "url_name": "projects"},
        {"name": "Skills", "url_name": "skills"},
        {"name": "Certifications", "url_name": "certifications"},
        {"name": "Contact", "url_name": "contact"},
    ]
    return render(request, 'home.html', {'nav_items': nav_items})


def education_details(request):
    education_list = Education.objects.all().order_by('-year')
    return render(request, 'education.html', {'education_list': education_list})

def internships(request):
    internships_list = Internship.objects.all()  # If using DB
    # OR use static data if no DB
    # internships_list = [
    #     {"company": "TCS", "role": "Web Development Intern", "duration": "Jan 2024 - Mar 2024", "description": "Worked on frontend and backend using Django."},
    #     {"company": "Infosys", "role": "Python Intern", "duration": "Jun 2023 - Aug 2023", "description": "Developed scripts and automation tools."},
    # ]
    return render(request, 'internships.html', {'internships': internships_list})


def projects(request):
    # If using database
    projects_list = Project.objects.all()

    # Or use static data instead
    # projects_list = [
    #     {
    #         "title": "Personal Portfolio",
    #         "description": "A personal website built with Django and Bootstrap.",
    #         "technologies": "Django, HTML, CSS, JavaScript",
    #         "github_link": "https://github.com/yourusername/portfolio"
    #     },
    #     {
    #         "title": "E-commerce App",
    #         "description": "Built a shopping cart and payment integration system.",
    #         "technologies": "Python, Django, Stripe",
    #         "github_link": "https://github.com/yourusername/ecommerce"
    #     },
    # ]

    return render(request, 'projects.html', {'projects': projects_list})

def skills(request):
    # If using model
    skills_list = Skill.objects.all()

    # Or use static list
    # skills_list = [
    #     {"name": "Python", "level": "Advanced"},
    #     {"name": "Django", "level": "Intermediate"},
    #     {"name": "JavaScript", "level": "Intermediate"},
    #     {"name": "HTML", "level": "Advanced"},
    #     {"name": "CSS", "level": "Advanced"},
    #     {"name": "MySQL", "level": "Intermediate"},
    # ]

    return render(request, 'skills.html', {'skills': skills_list})

def certifications(request):
    # Use from model
    certs = Certification.objects.all().order_by('-date_awarded')

    # Or use a static list:
    # certs = [
    #     {"title": "Python for Everybody", "issuer": "Coursera", "date_awarded": "2023-06-15", "url": "https://..."},
    #     {"title": "Django Development", "issuer": "Udemy", "date_awarded": "2022-12-01", "url": ""},
    # ]

    return render(request, 'certifications.html', {'certifications': certs})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Message from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = [settings.EMAIL_HOST_USER]
            try:
                send_mail(subject, message, sender, recipients)
                messages.success(request, "Your message has been sent successfully.")
                return redirect('contact')
            except BadHeaderError:
                messages.error(request, "Invalid header found.")
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})