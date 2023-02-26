from django.urls import path

from campaigns.views import CampaignList, CaseDetailView


app_name = "api_campaigns"

urlpatterns = [
    path("", CampaignList.as_view(), name='campaign-list'),
    path("<int:pk>/", CaseDetailView.as_view(), name='campaign-detail'),
]


