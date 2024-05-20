from django.db import models


# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    titles = models.ManyToManyField(Title)
    summary = models.TextField()
    image = models.ImageField(upload_to="profiles/")
    cv = models.FileField(upload_to="cvs/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company_name}"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    feedback = models.TextField()
    photo = models.ImageField(upload_to="testimonials/")
    creation_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.title}"


class WhatIDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Knowledge(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=255)
    start_year = models.DateField()
    end_year = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.school}"


class Certification(models.Model):
    title = models.CharField(max_length=100)
    cert_id = models.CharField(max_length=50)
    date = models.DateField()
    logo = models.ImageField(upload_to="certifications/")

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject
