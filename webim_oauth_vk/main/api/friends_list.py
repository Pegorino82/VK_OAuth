from django.http import JsonResponse

from django.contrib.auth.models import User
from main.models import Friends

import vk

VERSION_API = 5.92


def friends_list(request, *args, **kwargs):
    social_vk = request.user.social_auth.get(provider='vk-oauth2')
    access_token = social_vk.extra_data.get('access_token')
    vk_user_id = social_vk.uid

    session = vk.Session(access_token=access_token)
    vk_api = vk.API(session)
    vk_user_friends = vk_api.friends.get(
        user_id=vk_user_id,
        order='random',
        count=5,
        fields=('nickname', 'photo_50'),
        v=VERSION_API
    )
    friends = vk_user_friends['items']
    result = {'results': friends}

    user = User.objects.get(username=request.user)

    last_friends = Friends.objects.filter(user=user)
    if last_friends:
        last_friends.delete()

    for friend in friends:

        friend.pop('is_closed', '')
        friend.pop('can_access_closed', '')
        friend.pop('online', '')
        friend.pop('lists', '')
        Friends.objects.create(
            user=user,
            friend=friend
        )

    return JsonResponse(result, charset='utf-8')
