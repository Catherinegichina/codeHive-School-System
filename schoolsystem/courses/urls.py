from django.urls import path
from .views import course_list, course_profile, delete_course, edit_course, register_courses
app_name="courses"
urlpatterns = [
    path("register/", register_courses, name="register_courses"),
    path("list/", course_list, name="course_list"),
    path("edit/<int:id>/", edit_course, name="edit_course"),
    path("profile/<int:id>/", course_profile, name="course_profile"),
    path("delete/<int:id>/", delete_course, name="delete_course"),
]