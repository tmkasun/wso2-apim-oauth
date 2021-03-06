from django.shortcuts import render
from oauth_playground.configs import Configs


def index(request):
    cont = {
        'callback_url': Configs.get_callback_url(),
        'facebook_auth_url': Configs.facebook['auth_endpoint'],
        'wso2_auth_url': Configs.wso2['auth_endpoint'],
        'wso2_scope': Configs.wso2['scope'],
        'facebook_scope': Configs.facebook['scope']
    }
    return render(request, 'home/index.html', cont)
