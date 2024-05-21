from django.contrib import admin
from resume.models import (
    Title,
    Tag,
    SocialMedia,
    Profile,
    WhatIDo,
    Testimonial,
    Education,
    Experience,
    Knowledge,
    Certification,
    Contact,
    SkillCategory,
    Skill,
    PortfolioCategory,
    Portfolio,
    PortfolioImage,
    BlogCategory,
    Blog,
    BlogImage,
)


# Register your models here.
@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    filter_horizontal = ("titles", "social_media")


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category__name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "title")
    list_filter = ("creation_date",)


@admin.register(WhatIDo)
class WhatIDoAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    search_fields = ("title", "category__name")
    list_filter = ("category__name",)
    filter_horizontal = ("tags",)
    inlines = [PortfolioImageInline]


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    search_fields = ("title", "category__name")
    list_filter = ("category__name",)
    filter_horizontal = ("tags",)
    inlines = [BlogImageInline]


@admin.register(Contact)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject")
    list_filter = ("created_at",)
