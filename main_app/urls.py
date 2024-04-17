from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('traits/', views.TraitList.as_view(), name='traits_index'),
    path('traits/<int:pk>/', views.TraitDetail.as_view(), name='traits_detail'),
    path('traits/create/', views.TraitCreate.as_view(), name='traits_create'),
    path('traits/<int:pk>/update/', views.TraitUpdate.as_view(), name='traits_update'),
    path('traits/<int:pk>/delete/', views.TraitDelete.as_view(), name='traits_delete'),
    path('dogs/<int:dog_id>/assoc_trait/<int:trait_id>/', views.assoc_trait, name='assoc_trait'),
    path('dogs/<int:dog_id>/remove_trait/<int:trait_id>/', views.remove_trait, name='remove_trait'),
]