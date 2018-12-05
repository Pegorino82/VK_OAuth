from django.urls import path, include

from main.views import login_view, logout_view, index_view

app_name = 'mainapp'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('index/', index_view, name='index'),
]
