from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path(route='',                   view=views.index,      name='index'),
    path(route='tags/',              view=views.tags,       name='tags'),
    path(route='<int:note_id>/',     view=views.note_view,  name='note_view'),
    path(route='notes_by_tag/<int:tag_id>/', view=views.notes_by_tag,  name='notes_by_tag'),
]