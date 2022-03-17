from django.urls import path

from petstagram.main.views import show_home, show_dashboard, show_profile, show_pet_photo_details, like_pet_photo, \
    create_profile, edit_profile, delete_profile, create_pet, edit_pet, delete_pet, create_pet_photo, edit_pet_photo

urlpatterns = [
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/add/', create_pet_photo, name='create pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('pets/create', create_pet, name='create pet'),
    path('pet/edit', edit_pet, name='edit pet'),
    path('pet/delete', delete_pet, name='delete pet'),
]
