from rest_framework import serializers
from .models import LeaveRequest, SiteIssue

class LeaveRequestSerializer(serializers.ModelSerializer):
    requested_by_data = serializers.SerializerMethodField()
    can_approve = serializers.SerializerMethodField()
    class Meta:
        model = LeaveRequest
        fields = "__all__"
        
    def get_requested_by_data(self, obj):
        return {
            "id": obj.requested_by.id,
            "username": obj.requested_by.username,
            "email": obj.requested_by.email,
        }
        
    def get_can_approve(self, obj):
        user = self.context.get("user")
        if user.is_staff:
            return True
        return False
        
class SiteIssueSerializer(serializers.ModelSerializer):
    reported_by_data = serializers.SerializerMethodField()
    resolved_by_data = serializers.SerializerMethodField()
    can_resolve = serializers.SerializerMethodField()
    status = serializers.CharField(read_only=True)
    
    class Meta:
        model = SiteIssue
        fields = "__all__"
        
    def get_reported_by_data(self, obj):
        return {
            "id": obj.reported_by.id,
            "username": obj.reported_by.username,
            "email": obj.reported_by.email,
        }
        
    def get_resolved_by_data(self, obj):
        if obj.resolved_by:
            return {
                "id": obj.resolved_by.id,
                "username": obj.resolved_by.username,
                "email": obj.resolved_by.email,
            }
        return None
    
    def get_can_resolve(self, obj):
        user = self.context.get("user")
        if user.is_staff:
            return True
        return False