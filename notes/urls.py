from django.urls import path
from .views import NoteListView
# from .views import NotesView
# from .views import getNotes, getNote, updateNote, deleteNote, createNote

urlpatterns = [
    path('', NoteListView.as_view({'get': 'list', 'post': 'create'})),
    path('/<str:pk>', NoteListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # path('notes', NotesView.as_view()),


    # path('notes', getNotes, name="notes"),
    # path('notes/create', createNote, name="create"),
    # path('notes/<str:pk>/update', updateNote, name="update"),
    # path('notes/<str:pk>/delete', deleteNote, name="delete"),
    # path('notes/<str:pk>', getNote, name="note"),
]

