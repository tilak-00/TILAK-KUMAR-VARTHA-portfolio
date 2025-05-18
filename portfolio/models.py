from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Internship(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.company} - {self.role}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200, default='Not Specified')

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Advanced
    category = models.CharField(max_length=50, blank=True)  # Optional: e.g., Frontend, Backend

    def __str__(self):
        return self.name

class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_awarded = models.DateField()
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title