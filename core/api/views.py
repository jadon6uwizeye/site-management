from rest_framework import generics
from .models import LeaveRequest, SiteIssue
from .serializers import LeaveRequestSerializer, SiteIssueSerializer
from rest_framework.permissions import IsAuthenticated

class LeaveRequesCreateAPIView(generics.CreateAPIView):
    queryset = LeaveRequest.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LeaveRequestSerializer
    
    def perform_create(self, serializer):
        serializer.save(requested_by=self.request.user)

class SiteIssueCreateAPIView(generics.CreateAPIView):
    queryset = SiteIssue.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SiteIssueSerializer
    
    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)