from django.db import router
from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import EventViewSet, StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet

router = routers.DefaultRouter()
router.register("students/", StudentViewSet)
router.register("trainers/", TrainerViewSet)
router.register("courses/", CourseViewSet)
router.register("events/", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
]