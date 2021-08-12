from rest_framework import serializers
from .models import notify, group_notify

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = group_notify
        fields = ('message', 'target_contacts', 'uuid')

class CustomeSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    total_count = serializers.IntegerField()
    is_executed= serializers.BooleanField()
    # successful = serializers.IntegerField()
    # failed = serializers.IntegerField()
    message = serializers.CharField()

class ErrorSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()

    def error_check(self, request_data):
        obj = group_notify.objects.get(uuid=request_data['UUID'])
        if obj:
            return
        else:
            raise serializers.ErrorDetail({'Error':'Invalid UUID'})



class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = notify
        fields = ( 'destination_device_id', 'group_id', 'is_sent' )