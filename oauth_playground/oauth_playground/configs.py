class Configs(object):
    facebook = {
        'auth_endpoint': "https://www.facebook.com/dialog/oauth",
        'token_endpoint': "https://graph.facebook.com/oauth/access_token",
        'client_id': '347009092299227',  # app_id
        'client_secret': '6c1493a73459a238826f0f23a6250ef5',  # app_secret
        'scope': 'public_profile',
        'resource_endpoint': 'https://graph.facebook.com'
    }
    wso2 = {
        'auth_endpoint': "https://localhost:8243/authorize",
        'token_endpoint': "https://localhost:8243/token",
        'client_id': 'fMl9fqQu3GF5rGfcSeGhqX8PB00a',  # Consumer Key
        'client_secret': 'vGk7XPnf0tLM8gfihT_YLQQO9c4a',  # Consumer Secret
        'scope': 'get_book'
    }
    commons = {
        'callback': {
            'host': 'localhost',
            'port': '8000',
            'ssl': False,
            'context': '/oauth/callback/'
        }
    }

    @staticmethod
    def get_callback_url():
        return Configs._protocol(
                Configs.commons['callback']['ssl']) + "://" \
               + Configs.commons['callback']['host'] + ":" \
               + Configs.commons['callback']['port'] \
               + Configs.commons['callback']['context']

    @staticmethod
    def _protocol(ssl=False):
        return 'https' if ssl else 'http'
