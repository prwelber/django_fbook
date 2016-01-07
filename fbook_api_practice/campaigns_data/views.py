from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import Campaign, AdAccount, AdSet, Insights, Ad
import os

# Create your views here.
# Kim Crawford campaign ID# 6039958653409

def index(request):
    print(request)
    return render(request, 'campaigns_data/index.html')


def data(request):
    print(request)
    # environmental variables for facebook auth
    app_id = os.environ['APP_ID']
    app_secret = os.environ['APP_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    FacebookAdsApi.init(app_id, app_secret, access_token)

    campaign_id = request.GET['campaign-id']

    def get_campaign_stats(campaign):
        campaign = Campaign(campaign)
        params = {
            'data_preset': 'lifetime',
            'fields': [
                Insights.Field.impressions,
                Insights.Field.unique_clicks,
                Insights.Field.reach,
                Insights.Field.cpm,
                Insights.Field.spend,
            ]
        }
        data_set = campaign.get_insights(params=params)
        return data_set[0]

    data_set = get_campaign_stats(campaign_id)
    data_set['cpm'] = str(data_set['cpm'])[:4]
    context = {
        'data_set': data_set,
        'name': 'Campaign Breakdown',
    }
    print(data_set)
    return render(request, 'campaigns_data/data.html', context)
