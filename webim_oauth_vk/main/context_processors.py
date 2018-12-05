from main.models import Friends
import json


def friends(request):
    friends = []
    if request.user.is_authenticated:
        raw_friends = Friends.objects.filter(user=request.user)
        for f in raw_friends:
            a = f.friend.replace("'", '"')
            try:
                j = json.loads(a)
                friends.append(j)
            except Exception as err:
                print(err)

    return {
        'friends': friends
    }
