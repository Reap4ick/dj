from django.urls import path

from products import views

urlpatterns = [
    path("home/", views.home),
    path("list/", views.list),
    path("create/", views.create),
    path("edit/<int:id>", views.edit, name="edit"),
    path("details/<int:id>", views.details, name="details"),
    path("delete/<int:id>", views.delete, name="delete"),

]