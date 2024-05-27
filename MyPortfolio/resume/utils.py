from resume.models import Profile, Portfolio, Blog
from django.utils import timezone


def global_context():
    current_year = timezone.now().year

    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist:
        profile = None

    recent_projects = Portfolio.objects.order_by("-id")[:5]
    recent_posts = Blog.objects.filter(status="published").order_by("-id")[:5]

    return {
        "current_year": current_year,
        "profile": profile,
        "recent_projects": recent_projects,
        "recent_posts": recent_posts,
    }
