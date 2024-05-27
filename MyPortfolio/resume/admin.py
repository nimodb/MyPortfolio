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
    Language,
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
    list_display = ("title", "url", "icon")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    filter_horizontal = ("titles", "social_media")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "level")


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "percentage")
    list_filter = ("category",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name", "start_date", "end_date", "current")
    search_fields = ("title", "company_name")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "creation_date")
    list_filter = ("creation_date",)


@admin.register(WhatIDo)
class WhatIDoAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "start_date", "end_date")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "cert_id", "date")


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
    list_filter = ("category", "creation_date")
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
    list_display = (
        "title",
        "category",
        "creator",
        "created_at",
        "updated_at",
        "view_count",
        "status",
    )
    list_editable = ("status",)
    search_fields = ("title", "category")
    list_filter = ("category", "status")
    filter_horizontal = ("tags",)
    inlines = [BlogImageInline]


@admin.register(Contact)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "created_at")
    list_filter = ("created_at",)
