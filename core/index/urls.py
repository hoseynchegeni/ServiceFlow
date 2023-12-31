from django.urls import path
from .views import IndexView
from django.contrib.auth.decorators import login_required

app_name = "index"
urlpatterns = [
    path("", login_required(IndexView.as_view()), name="home"),
]
