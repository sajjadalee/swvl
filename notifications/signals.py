from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from notifications.models import *
from notifications.tasks import send_notifications


@receiver(post_save, sender=group_notify)
def save_grp_notify_model(sender, **kwargs):
    send_notifications.delay()