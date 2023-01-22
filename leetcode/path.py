INSTALLED_APPS = [
     #추가
    'channels',
    'alarms',
]
#추가
ASGI_APPLICATION = 'wesoket.routing.application'
#DIRS 부분만 변경
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'alarms')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#channel_layers 추가
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


from channels.routing import ProtocolTypeRouter, URLRouter
import alarms.routing
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
            alarms.routing.websocket_urlpatterns
        )
})

from django.db import models

class Alarm(models.Model):
    message=models.CharField(max_length=100)