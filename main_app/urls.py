from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Define the home route
    path('', views.home, name='home'),
    # about page route
    path('about/', views.about, name='about'),
    # shows all cats
    path('cats/', views.cats_index, name='cat-index'),
    # Updated to use the new cat_detail view
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),  
    # Route for adding a feeding to a specific cat
    path(
        'cats/<int:cat_id>/add-feeding/', 
        views.add_feeding, 
        name='add-feeding'
    ),

    # Routes for class-based views for Cat CRUD operations
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    # Routes for class-based views for Toy CRUD operations
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    # New URL to associate a toy with a cat
    path('cats/<int:cat_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    # and to remove a toy from a cat (optional)
    path('cats/<int:cat_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),


]