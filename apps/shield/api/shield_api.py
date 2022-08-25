from cgi import test
from datetime import date
from typing import List
from drf_rw_serializers.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from apps.shield.services.malicious_link_detection import malicious_link_detection
from django_filters.rest_framework import DjangoFilterBackend
from apps.user.constants.user_constants import DELETE_SUCCESS


class MaliciousLinkDetectionAPI(ListCreateAPIView):
    
    """
        Email Security API
    """

    def post(self, request, *args, **kwargs):
        test_link = request.data.get("test_url", None)
        test_link = test_link if type(test_link) == list else [test_link]

        result = malicious_link_detection(test_link)
        print(result)
        return Response({'success':True, 'url_result':result})
