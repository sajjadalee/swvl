from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = 'notifications'  ## write your app name here

    def ready(self):
        import notifications.signals