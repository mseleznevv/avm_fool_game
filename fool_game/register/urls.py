from django.urls import path

from . import views

app_name = "register"
urlpatterns = [
    path("", views.index, name="index"),
    path("user/<int:user_id>/", views.get_user, name="get_user")
]

