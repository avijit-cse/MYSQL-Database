from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name="index"),
    path('list/<int:a_id>/',views.album_list,name="album_list"),
    path('mf/',views.misician_form,name="misician_form"),
    path('af/',views.album_form,name="album_form"),
    path('edit/<int:a_id>/',views.editview,name="editview"),
    path('aedit/<int:b_id>/',views.edit_album,name="edit_album"),
    path('delect/<int:album_id>/',views.delectview,name="delectview"),
    path('mdelect/<int:ab_id>/',views.mdelectview,name="mdelectview"),
    
]
