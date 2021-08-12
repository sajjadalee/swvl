from swvl_project.celery_app import app as celery_app
from celery import shared_task
import time
from .models import group_notify, notify

@shared_task
def send_notifications():
    try:
        new_notification = group_notify.objects.latest('date_created')
        if new_notification:
            print("UUID for this batch : {}".format(new_notification.uuid))
            lst_of_targets = new_notification.target_contacts.split("|")
            for items in lst_of_targets:
                print("sending notification to user : {}".format(items))
                #TODO: write a method to connect with 3rd party SMS aggregator
                # and sed SMS with content new_notification["message"]
                notification = notify.objects.create(destination_device_id = items, group_id = new_notification,
                                                     is_sent=True)
        else:
            print("No notification yet, feed me more notifications")
                    # print("Notification Successfully Sent to {}".format())

    except:
        print("unable to process".format())
    finally:
        group_notify.objects.filter(id=new_notification.id).update(is_executed=True)



    # conn = celery_app.broker_connection().default_channel.client
    # counter = conn.get('print_hello')
    # print(counter)
    # print("Hello from the new world")

