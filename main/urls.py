from django.urls import path
from main import views

urlpatterns = [
    path("author", views.author),
    path("book", views.book),
    path("pub", views.publication),
    path("stu", views.stu),
    path("tchr", views.tchr),
    path("data", views.detail),
]
