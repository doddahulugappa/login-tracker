from django.contrib.auth import user_logged_in,user_logged_out
from django.dispatch.dispatcher import receiver
from .models import UserSession

@receiver(user_logged_in)
def on_user_logged_in(**kwargs):
    UserSession.objects.get_or_create(user=kwargs.get('user'))

@receiver(user_logged_out)
def on_user_logged_out(**kwargs):
    UserSession.objects.filter(user=kwargs.get('user')).delete()