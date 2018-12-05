from django.urls import path

from main.api.friends_list import friends_list

app_name = 'rest_friends'

urlpatterns = [
    path('list/', friends_list, name='rest_list'),
]