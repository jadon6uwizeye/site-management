from rest_framework import generics
from .models import LeaveRequest, SiteIssue
from .serializers import LeaveRequestSerializer, SiteIssueSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

class LeaveRequesListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = LeaveRequestSerializer
    
    def perform_create(self, serializer):
        user = get_user_model().objects.all().first()
        print("user", user)
        serializer.save(requested_by=user)

class SiteIssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = SiteIssue.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = SiteIssueSerializer
    
    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)