from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("page/<int:page>", views.page, name="home"),
    path("details/<str:pk>", views.details, name="details"),
    path("register", views.register_user, name="register"),
    path("login", views.login_user, name="login"),
    # path("profile", views.profile, name="profile"),
    path("logout", views.logout_user, name="logout"),
    path("add_comment, <str:pk>", views.add_comment, name="add_comment"),
    path("add_blog", views.add_blog, name="add_blog"),
    path("delete_blog, <str:pk>", views.delete_blog, name="delete_blog"),
    path("search", views.search, name="search"),
]