from django.urls import path, include, re_path
from rest_framework import routers

from apps.shield.api.shield_api import MaliciousLinkDetectionAPI, SpamContentDetectionAPI


urlpatterns = (
    path("malicious-url/", MaliciousLinkDetectionAPI.as_view()),
    path("malicious-content/", SpamContentDetectionAPI.as_view())
)
