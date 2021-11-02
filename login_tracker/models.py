from django.db import models
from django.conf import settings
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='logged_in_user',on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32,null=True,blank=True)

    def __str__(self):
        return self.user.username

class LoginHistoryTracker(models.Model):
    """
    model for tracking logins
    """
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    host = models.CharField(max_length=256,null=True)
    user_agent = models.CharField(max_length=1024,null=True)
    username = models.CharField(max_length=256,null=True)
    date_time = models.DateTimeField(blank=True,null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Login History Tracker"

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action,self.username,self.date_time)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action,self.username,self.date_time)

@receiver(user_logged_in)
def user_logged_in_callback(request,user,**kwargs):
    ip = request.META.get("REMOTE_ADDR")
    host = request.META.get("HTTP_HOST")
    user_agent = request.META.get("HTTP_USER_AGENT")
    date_time = timezone.now()
    LoginHistoryTracker.objects.create(action='user_logged_in',
                                       ip=ip,
                                       username=user.username,
                                       date_time=date_time,
                                       host=host,
                                       user_agent=user_agent)

@receiver(user_logged_out)
def user_logged_in_callback(request,user,**kwargs):
    ip = request.META.get("REMOTE_ADDR")
    host = request.META.get("HTTP_HOST")
    user_agent = request.META.get("HTTP_USER_AGENT")
    date_time = timezone.now()
    LoginHistoryTracker.objects.create(action='user_logged_out',
                                       username=user.username,
                                       date_time=date_time,
                                       host=host,
                                       ip=ip,
                                       user_agent=user_agent)

@receiver(user_login_failed)
def user_logged_in_callback(request,credentials,**kwargs):
    ip = request.META.get("REMOTE_ADDR")
    host = request.META.get("HTTP_HOST")
    user_agent = request.META.get("HTTP_USER_AGENT")
    date_time = timezone.now()
    LoginHistoryTracker.objects.create(action='user_login_failed',
                                       username=credentials.get('username',None),
                                       date_time=date_time,
                                       host=host,
                                       ip=ip,
                                       user_agent=user_agent)