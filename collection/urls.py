from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("artwork/<int:artwork_id>", views.artwork, name="artwork"),
    path("artworks/search", views.search_artworks, name="search_artworks"),
    path("accounts/profile/", views.index, name="profile"),  
    path("accounts/register/", views.register, name="register"),
    path("artworks/random", views.random_artworks, name="random_artworks"), 
    path("collections/", views.collections, name="collections"),
    path("collection_list/", views.collection_list, name="collection_list"),
    path("collection/add", views.collection_add, name="collection_add"),
    path('collection/<int:collection_id>/', views.details, name='details'),
    path('artwork/<int:artwork_id>/add-to-collection/', views.add_to_collection, name='add_to_collection'),
    path('collection/<int:collection_id>/remove/<int:artwork_id>/', views.remove_from_collection, name='remove_from_collection'),
    path('collection/<int:collection_id>/edit/', views.collection_edit, name='collection_edit'),
    path('collection/remove/<int:collection_id>/', views.remove_collection, name='remove_collection'),
    path('artist_artworks/<slug:artist_slug>/', views.artist_artworks, name='artist_artworks'),



]