from rest_framework import serializers
from .models import LeaveRequest, SiteIssue

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = "__all__"
        
class SiteIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteIssue
        fields = "__all__"