from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "icon")


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    filter_horizontal = ("titles", "social_media")


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "level")


@admin.register(models.SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "percentage")
    list_filter = ("category",)


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name", "start_date", "end_date", "current")
    search_fields = ("title", "company_name")


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "creation_date")
    list_filter = ("creation_date",)


@admin.register(models.WhatIDo)
class WhatIDoAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(models.Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "start_date", "end_date")


@admin.register(models.Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "cert_id", "date")


@admin.register(models.PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PortfolioImageInline(admin.TabularInline):
    model = models.PortfolioImage
    extra = 1


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    search_fields = ("title", "category__name")
    list_filter = ("category", "creation_date")
    filter_horizontal = ("tags",)
    inlines = [PortfolioImageInline]


@admin.register(models.BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


class BlogImageInline(admin.TabularInline):
    model = models.BlogImage
    extra = 1


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    autocomplete_fields = ["category"]
    list_display = (
        "title",
        "category",
        "creator",
        "created_at",
        "updated_at",
        "view_count",
        "reading_time",
        "status",
    )
    list_editable = ("status",)
    search_fields = ("title", "category")
    list_filter = ("category", "status")
    filter_horizontal = ("tags",)
    inlines = [BlogImageInline]


@admin.register(models.Contact)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "created_at")
    list_filter = ("created_at",)
