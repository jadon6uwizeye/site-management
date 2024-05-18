from rest_framework import generics
from .models import LeaveRequest, SiteIssue
from .serializers import LeaveRequestSerializer, SiteIssueSerializer

class LeaveRequesCreateAPIView(generics.CreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class SiteIssueCreateAPIView(generics.CreateAPIView):
    queryset = SiteIssue.objects.all()
    serializer_class = SiteIssueSerializer