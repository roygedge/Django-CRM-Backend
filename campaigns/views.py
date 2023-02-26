from rest_framework import generics
from campaigns.models import Campaign
from campaigns.serializer import CampaignSerializer
from rest_framework.views import APIView

import json

from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from drf_yasg import openapi

from accounts.models import Account
from accounts.serializer import AccountSerializer
from campaigns import swagger_params
from campaigns.models import Campaign
from common.models import Attachments, Comment, Profile

# from common.custom_auth import JSONWebTokenAuthentication
from common.utils import CASE_TYPE, PRIORITY_CHOICE, STATUS_CHOICE
from contacts.models import Contact
from contacts.serializer import ContactSerializer


class CampaignList(APIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    @swagger_auto_schema(tags=["Campaigns"])
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return Response(context)


    @swagger_auto_schema(tags=["Campaigns"])
    def post(self, request, *args, **kwargs):
        params = request.post_data
        serializer = CaseCreateSerializer(data=params, request_obj=request)
        if serializer.is_valid():
            
            #Add edit to the parameters.

            return Response(
                {"error": False, "message": "Case Created Successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": True, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

@swagger_auto_schema(
  
)
class CaseDetailView(APIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    
    permission_classes = (IsAuthenticated,)
    model = Campaign

    def get_object(self, pk):
        return self.model.objects.filter(id=pk  ).first()



    @swagger_auto_schema(tags=["Campaigns"])
    def delete(self, request, pk, format=None):
        self.object = self.get_object(pk)
        if self.object.org != request.org:
            return Response(
                {"error": True, "errors": "User company doesnot match with header...."},
                status=status.HTTP_403_FORBIDDEN,
            )
        if self.request.profile.role != "ADMIN" and not self.request.profile.is_admin:
            if self.request.profile != self.object.created_by:
                return Response(
                    {
                        "error": True,
                        "errors": "You do not have Permission to perform this action",
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )
        self.object.delete()
        return Response(
            {"error": False, "message": "Case Deleted Successfully."},
            status=status.HTTP_200_OK,
        )

