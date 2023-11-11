from django.urls import path
from . import views


urlpatterns = [
    path('', views.NoteListView.as_view(), name="home"),
    path('add', views.NoteCreateView.as_view(), name="add_note"),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name="note_detail"),
    path('note/<int:pk>/update', views.NoteUpdateView.as_view(), name="note_update"),
    path('note/<int:pk>/delete', views.NoteDeleteView.as_view(), name="note_delete"),
]