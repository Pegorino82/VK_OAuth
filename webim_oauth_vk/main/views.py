from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth import logout

from main.models import Friends


def login_view(request, *args, **kwargs):
    template_name = 'main/login.html'
    is_authenticated_url = reverse_lazy('mainapp:index')
    context = {}
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.user.social_auth.get(user_id=user_id):
            return redirect(is_authenticated_url)
    return render(request, template_name, context)


def logout_view(request, *args, **kwargs):
    last_friends = Friends.objects.filter(user=request.user)
    last_friends.delete()
    success_url = reverse_lazy('mainapp:login')
    logout(request)
    return redirect(success_url)


def index_view(request, *args, **kwargs):
    template_name = 'main/index.html'
    none_authenticated_url = reverse_lazy('mainapp:login')
    if request.user.is_authenticated:
        return render(request, template_name, {})
    else:
        return redirect(none_authenticated_url)
