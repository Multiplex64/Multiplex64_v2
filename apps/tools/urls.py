from django.urls import path

from . import views

app_name = "tools"
urlpatterns = [
    path("", views.index, name="index"),
    path('<path:template_name>/', views.tool, name='tool'),
]