from django.urls import path
from resume.views import (
    HomeView,
    ContactView,
    ResumeView,
    BlogView,
    BlogDetailView,
    PortfolioView,
    PortfolioDetailView,
)

app_name = "resume"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("resume/", ResumeView.as_view(), name="resume"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
    path("portfolio/<int:pk>/", PortfolioDetailView.as_view(), name="portfolio_detail"),
]
