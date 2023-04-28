from django.urls import Path
from .views import Homepage

urlpatterns = [
    path("", Homepage.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
]
