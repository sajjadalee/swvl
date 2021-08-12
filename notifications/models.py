from django.db import models
import uuid
from datetime import datetime
from django.core.validators import RegexValidator

# Create your models here.
class group_notify(models.Model):
    message = models.CharField(max_length=500)
    # TODO: apply RegEx to validate data in target_contacts
    # target_contacts = models.CharField(max_length=1000, validators=[RegexValidator(
    #         regex= '^[a-zA-Z0-9]*$',
    #         message='Only Numbers Allowed separated with |',
    #         code='invalid_numbers'
    #     ),])
    target_contacts = models.CharField(max_length=1000)
    total_count = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid1())
    is_executed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.message

class notify(models.Model):
    destination_device_id = models.CharField(max_length=100)
    group_id = models.ForeignKey(group_notify, on_delete= models.CASCADE, related_name='grp_notify')
    is_sent = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.destination_device_id






