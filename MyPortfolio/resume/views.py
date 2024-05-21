from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from resume.models import (
    Education,
    Experience,
    Certification,
    SkillCategory,
    Knowledge,
    WhatIDo,
    Testimonial,
    Blog,
    Portfolio,
    PortfolioCategory,
)
from resume.forms import ContactForm
from resume.utils import global_context


# Create your views here.
class HomeView(TemplateView):
    template_name = "resume/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(global_context())
        context.update(self.get_what_i_do_context())
        context.update(self.get_testimonial_context())
        context.update(self.get_meta_tags())
        return context

    def get_what_i_do_context(self):
        what_i_do_list = WhatIDo.objects.all()
        return {"what_i_do_list": what_i_do_list}

    def get_testimonial_context(self):
        testimonial_list = Testimonial.objects.all()
        return {"testimonial_list": testimonial_list}

    def get_meta_tags(self):
        return {
            "meta_title": "NONE NAME",
            "meta_description": "NONE NAME",
            "meta_keywords": "NONE NAME",
            "meta_author": "NONE NAME",
        }


class ResumeView(TemplateView):
    template_name = "resume/resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(global_context())
        context.update(self.get_education_context())
        context.update(self.get_experience_context())
        context.update(self.get_skill_context())
        context.update(self.get_knowledge_context())
        context.update(self.get_certification_context())
        context.update(self.get_meta_tags())
        return context

    def get_education_context(self):
        education_list = Education.objects.all()
        return {"education_list": education_list}

    def get_experience_context(self):
        experience_list = Experience.objects.all()
        return {"experience_list": experience_list}

    def get_skill_context(self):
        skill_categories = SkillCategory.objects.prefetch_related("skill_set").all()
        return {"skill_categories": skill_categories}

    def get_knowledge_context(self):
        knowledge_list = Knowledge.objects.all()
        return {"knowledge_list": knowledge_list}

    def get_certification_context(self):
        certification_list = Certification.objects.all()
        return {"certification_list": certification_list}

    def get_meta_tags(self):
        return {
            "meta_title": "NONE NAME",
            "meta_description": "NONE NAME",
            "meta_keywords": "NONE NAME",
            "meta_author": "NONE NAME",
        }


class BlogView(ListView):
    model = Blog
    template_name = "resume/blog.html"
    context_object_name = "blog_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(global_context())
        context.update(self.get_meta_tags())
        return context

    def get_meta_tags(self):
        return {
            "meta_title": "NONE NAME",
            "meta_description": "NONE NAME",
            "meta_keywords": "NONE NAME",
            "meta_author": "NONE NAME",
        }


class BlogDetailView(DetailView):
    model = Blog
    template_name = "resume/blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(global_context())
        context.update(self.get_next_prev_items(self.object))
        context.update(self.get_meta_tags())
        return context

    def get_next_prev_items(self, current_item):
        next_item = Blog.objects.filter(id__gt=current_item.id).order_by("id").first()
        prev_item = Blog.objects.filter(id__lt=current_item.id).order_by("-id").first()

        return {"next_item": next_item, "prev_item": prev_item}

    def get_meta_tags(self):
        return {
            "meta_title": "NONE NAME",
            "meta_description": "NONE NAME",
            "meta_keywords": "NONE NAME",
            "meta_author": "NONE NAME",
        }


class PortfolioView(ListView):
    model = Portfolio
    template_name = "resume/portfolio.html"
    context_object_name = "portfolio_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(global_context())
        context.update(self.get_category_context())
        context.update(self.get_meta_tags())
        return context

    def get_category_context(self):
        category_list = PortfolioCategory.objects.all()
        return {"category_list": category_list}

    def get_meta_tags(self):
        return {
            "meta_title": "NONE NAME",
            "meta_description": "NONE NAME",
            "meta_keywords": "NONE NAME",
            "meta_author": "NONE NAME",
        }


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "resume/portfolio_detail.html"
    context_object_name = "portfolio"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(global_context())
        context.update(self.get_next_prev_items(self.object))
        context.update(self.get_meta_tags())
        return context

    def get_next_prev_items(self, current_item):
        next_item = (
            Portfolio.objects.filter(id__gt=current_item.id).order_by("id").first()
        )
        prev_item = (
            Portfolio.objects.filter(id__lt=current_item.id).order_by("-id").first()
        )

        return {"next_item": next_item, "prev_item": prev_item}

    def get_meta_tags(self):
        return {
            "meta_title": "NONE NAME",
            "meta_description": "NONE NAME",
            "meta_keywords": "NONE NAME",
            "meta_author": "NONE NAME",
        }


class ContactView(FormView):
    template_name = "resume/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("resume:contact")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(global_context())
        context.update(self.get_meta_tags())
        return context

    def get_meta_tags(self):
        return {
            "meta_title": "NONE NAME",
            "meta_description": "NONE NAME",
            "meta_keywords": "NONE NAME",
            "meta_author": "NONE NAME",
        }
