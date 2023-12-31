from django.urls import path
from .views import (
    PublicNoteView,
    MyNotesView,
    MyArchiveNotesView,
    CreatePublicNote,
    CreateNote,
    NoteUpdateView,
    NoteDetailView,
    NoteDeleteView,
    ListTagView,
    DisableTagView,
    CreateTagView,
    UpdateTagView,
    DeleteTagView,
    DetailTagView,
)

app_name = "notes"

urlpatterns = [
    path("public_notes/", PublicNoteView.as_view(), name="public_notes"),
    path("my_notes/", MyNotesView.as_view(), name="my_notes"),
    path("my_archive_notes/", MyArchiveNotesView.as_view(), name="my_archive_notes"),
    path("create_public_note/", CreatePublicNote.as_view(), name="create_public_note"),
    path("create_note/", CreateNote.as_view(), name="create_note"),
    path("detail/<int:pk>/", NoteDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", NoteDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", NoteUpdateView.as_view(), name="update"),
    path("tag_list/", ListTagView.as_view(), name="list_tag"),
    path("disable_tag/", DisableTagView.as_view(), name="disable_tag"),
    path("create/", CreateTagView.as_view(), name="create_tag"),
    path("update_tag/<int:pk>/", UpdateTagView.as_view(), name="update_tag"),
    path("detail_tag/<int:pk>/", DetailTagView.as_view(), name="detail_tag"),
    path("delete_tag/<int:pk>/", DeleteTagView.as_view(), name="delete_tag"),
]
