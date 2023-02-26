from rest_framework import serializers

from common.serializer import (AttachmentsSerializer, CommentSerializer,
                               ProfileSerializer)
from contacts.serializer import ContactSerializer
from campaigns.models import Campaign
from teams.serializer import TeamsSerializer

class CampaignSerializer(serializers.ModelSerializer):
    created_by = ProfileSerializer()
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignCreateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        request_obj = kwargs.pop("request_obj", None)
        super().__init__(*args, **kwargs)
        self.org = request_obj.org
        #self.fields["title"].required = True?

    def validate_campaign():
        pass

    
    class Meta:
        model = Campaign
        fields = (
            "id",
            "title",
            "status",
            "priority",
            "due_date",
            "account",
            "created_by",
            "created_on",
        )