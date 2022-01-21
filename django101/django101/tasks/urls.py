from django.urls import path

from django101.tasks.views import home, profile, profile_pic

urlpatterns = [
    path('', home),
    path('profile/', profile),
    path('profile/profile_pic', profile_pic)
]
