from django.urls import path

from . import views # Relative import(look file inside the same folder where the script is running.)

urlpatterns = [
    path("", views.index, name="index"),

    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")


]