from django.shortcuts import render
from petstagram.main.models import PetPhoto


def create_pet(request):
    return render(request, 'pet_create.html')


def edit_pet(request):
    return render(request, 'pet_edit.html')


def delete_pet(request):
    return render(request, 'pet_delete.html')
