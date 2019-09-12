from django.urls import path
from .views import NotesViews

app_name = "notes"

urlpatterns = [
    path('notes/',NotesViews.as_view()),
]