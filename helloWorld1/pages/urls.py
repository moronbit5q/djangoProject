from django.urls import path

from . import views

urlpatterns = [
    path("", views.homePageView, name="home"),
    path("settings/", views.settingPageView, name="settings")

]