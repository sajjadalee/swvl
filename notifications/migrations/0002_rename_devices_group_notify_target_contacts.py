# Generated by Django 3.2.6 on 2021-08-05 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_notify',
            old_name='devices',
            new_name='target_contacts',
        ),
    ]
