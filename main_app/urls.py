from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('places/', views.places_index, name='index'),
  path('places/<int:place_id>/', views.places_detail, name='detail'),
  path('places/create/', views.PlaceCreate.as_view(), name='places_create'),
  path('places/<int:pk>/update/', views.PlaceUpdate.as_view(), name='places_update'),
  path('places/<int:pk>/delete/', views.PlaceDelete.as_view(), name='places_delete'),
  path('places/<int:place_id>/add_visit/', views.add_visit, name='add_visit'),
  path('places/<int:place_id>/add_todo/', views.add_todo, name='add_todo'),
  path('places/<int:place_id>/add_photo/', views.add_photo, name='add_photo'),
  path('accounts/signup/', views.signup, name='signup'),
]