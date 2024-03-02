from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>/results/", views.results, name="results"),
    path("test/", views.test, name="test"),
    path("your-name/", views.your_name, name="your_name"),

]