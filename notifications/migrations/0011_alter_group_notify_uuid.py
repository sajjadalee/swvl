# Generated by Django 3.2.6 on 2021-10-15 11:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0010_alter_group_notify_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_notify',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('091ab63e-2da9-11ec-a71d-a509c8296b99')),
        ),
    ]
