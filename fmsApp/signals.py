# signals.py
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Post
from .blockchain import add_log, get_all_logs
from easyaudit.models import CRUDEvent

TYPES = {
    1: 'Create',
    2: 'Update',
    3: 'Delete'
}


@receiver(post_save, sender=CRUDEvent)
def log_post_save(sender, instance, **kwargs):
    print('we in')
    formatted_datetime = instance.datetime.strftime('%Y-%m-%d %H:%M:%S')

    add_log(
        method=TYPES[instance.event_type],
        content_type=instance.content_type.model,
        object_id=instance.object_id,
        object_name=instance.object_repr,
        user=instance.user.username,
        date=formatted_datetime
    )
    print(get_all_logs())
