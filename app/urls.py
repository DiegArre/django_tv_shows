from django.urls import path
from . import views

urlpatterns = [

    path("",views.start),
    path("shows",views.shows),
    path("shows/new", views.new_show),#GET
    path("shows/create",views.create_show),#POST
    path("shows/<int:id_show>", views.mostrar_show),
    path("shows/<int:id_show>/edit", views.edit_show),#GET
    path("shows/<int:id_show>/update", views.update_show),#POST
    path("shows/<int:id_show>/destroy", views.destroy_show)#POST
]