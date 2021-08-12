from django.http import Http404
from django.shortcuts import render

# Create your views here.

from rest_framework import status
from .models import notify, group_notify
from .serializers import GroupSerializer, CustomeSerializer, ErrorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
import uuid
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

class GroupNotifyView(APIView):
    authentication_classes = (SessionAuthentication,TokenAuthentication)
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        # try:
        result = {}
        try:
            total = notify.objects.values('group_id_id__message', 'group_id_id__is_executed', 'group_id_id__uuid').filter(
                group_id_id__uuid=request.data["uuid"]).annotate(total_count=Count('id'))

        except KeyError:
            raise Http404
        if total:
            for item in total:
                for key,value in item.items():
                    dict = {str(key).replace('group_id_id__','') : value}
                    result.update(dict)
        serializer = CustomeSerializer(result)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            total_targets = len(request.data['target_contacts'].split('|'))
            done =  serializer.save(total_count=total_targets, uuid=uuid.uuid1())
            respons = {"UUID" : done.uuid}
            return Response(respons)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

