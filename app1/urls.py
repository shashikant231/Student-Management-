from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("school", views.SchoolViewset)
router.register("student", views.StudentViewset)
router.register("student_info", views.StudentInfoViewset,basename="student_info")
router.register("book", views.BookViewset)


urlpatterns = [
    path("", include(router.urls)),
]+ router.urls
