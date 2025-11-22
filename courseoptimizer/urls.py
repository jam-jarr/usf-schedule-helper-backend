from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "get_suggested_courses",
        views.get_suggested_courses,
        name="get_suggested_courses",
    ),
]
