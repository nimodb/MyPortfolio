from bs4 import BeautifulSoup
import re
from django.db import models
from datetime import date
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
]


class Title(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    class Meta:
        verbose_name_plural = "Social Media"

    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    titles = models.ManyToManyField(Title)
    social_media = models.ManyToManyField(SocialMedia)
    summary = models.TextField()
    image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    cv_de = models.FileField(upload_to="cvs/de/", blank=True, null=True)
    cv_en = models.FileField(upload_to="cvs/en/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Language(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.level})"


class SkillCategory(models.Model):
    class Meta:
        verbose_name_plural = "Skill Categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Experience(models.Model):
    class Meta:
        ordering = ["-start_date"]

    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def duration(self):
        end_date = self.end_date if self.end_date and not self.current else date.today()
        delta = end_date - self.start_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        return f"{years} years, {months} months"

    def __str__(self):
        return f"{self.title} at {self.company_name}"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    feedback = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    creation_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.title}"


class WhatIDo(models.Model):
    class Meta:
        verbose_name_plural = "What I Do"

    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Knowledge(models.Model):
    class Meta:
        verbose_name_plural = "Knowledge"

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Education(models.Model):
    class Meta:
        ordering = ["-start_date"]

    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.school}"


class Certification(models.Model):
    title = models.CharField(max_length=100)
    cert_id = models.CharField(max_length=50)
    date = models.DateField()
    logo = models.ImageField(upload_to="certifications/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    class Meta:
        verbose_name_plural = "Portfolio Categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    creation_date = models.DateField()

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="portfolios/")

    def __str__(self):
        return f"Image for {self.portfolio.title}"


class BlogCategory(models.Model):
    class Meta:
        verbose_name_plural = "Blog Categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    class Meta:
        ordering = ["-created_at"]

    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    creator = models.CharField(max_length=200, default="NimoDB")
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    reading_time = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.reading_time = self.calculate_reading_time()
        super(Blog, self).save(*args, **kwargs)

    def calculate_reading_time(self):
        def strip_html_tags(text):
            soup = BeautifulSoup(text, "html.parser")
            return soup.get_text()

        text_without_html = strip_html_tags(self.content)
        words = re.findall(r"\w+", text_without_html)
        word_count = len(words)
        reading_speed = 200  # average reading speed in words per minute
        reading_time = word_count / reading_speed
        return round(reading_time)

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=["view_count"])


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/")

    def __str__(self):
        return f"Image for {self.blog.title}"


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
