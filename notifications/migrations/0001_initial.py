# Generated by Django 3.2.6 on 2021-08-05 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group_notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('devices', models.CharField(max_length=1000)),
                ('is_executed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_device_id', models.CharField(max_length=100)),
                ('is_sent', models.BooleanField(default=False)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.group_notify')),
            ],
        ),
    ]
