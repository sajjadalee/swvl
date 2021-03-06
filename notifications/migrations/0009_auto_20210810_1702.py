# Generated by Django 3.2.6 on 2021-08-10 12:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_auto_20210810_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_notify',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d7fcfc88-f9d2-11eb-85c4-08d40c3b3e1e')),
        ),
        migrations.AlterField(
            model_name='notify',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grp_notify', to='notifications.group_notify'),
        ),
    ]
