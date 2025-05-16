from django.urls import path
from my_stuff import views

urlpatterns = [
    path("", views.home, name="home"),
    path("package_detail/<int:package_id>", views.package_detail, name="package_detail"),
]
