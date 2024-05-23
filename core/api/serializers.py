from rest_framework import serializers
from .models import LeaveRequest, SiteIssue

class LeaveRequestSerializer(serializers.ModelSerializer):
    requested_by_data = serializers.SerializerMethodField()
    class Meta:
        model = LeaveRequest
        fields = "__all__"
        
    def get_requested_by_data(self, obj):
        return {
            "id": obj.requested_by.id,
            "username": obj.requested_by.username,
            "email": obj.requested_by.email,
            "first_name": obj.requested_by.first_name,
            "last_name": obj.requested_by.last_name,\
            "cell": obj.requested_by.userprofile.cell.name if obj.requested_by.userprofile.cell else "",
            "district": obj.requested_by.userprofile.district.name if obj.requested_by.userprofile.district else "",
            "office_level": obj.requested_by.userprofile.office_level.name if obj.requested_by.userprofile.office_level else "",
        }
        
        
class SiteIssueSerializer(serializers.ModelSerializer):
    reported_by_data = serializers.SerializerMethodField()
    resolved_by_data = serializers.SerializerMethodField()
    status = serializers.CharField(read_only=True)
    
    class Meta:
        model = SiteIssue
        fields = "__all__"
        
    def get_reported_by_data(self, obj):
        return {
            "id": obj.reported_by.id,
            "username": obj.reported_by.username,
            "email": obj.reported_by.email,
            "first_name": obj.reported_by.first_name,
            "last_name": obj.reported_by.last_name,
            "cell": obj.reported_by.userprofile.cell.name if obj.reported_by.userprofile.cell else "",
            "district": obj.reported_by.userprofile.district.name if obj.reported_by.userprofile.district else "",
            "office_level": obj.reported_by.userprofile.office_level.name if obj.reported_by.userprofile.office_level else "",
        }
        
    def get_resolved_by_data(self, obj):
        if obj.resolved_by:
            return {
                "id": obj.resolved_by.id,
                "username": obj.resolved_by.username,
                "email": obj.resolved_by.email,
                "first_name": obj.resolved_by.first_name,
                "last_name": obj.resolved_by.last_name,
                "cell": obj.resolved_by.userprofile.cell.name if obj.resolved_by.userprofile.cell else "",
                "district": obj.resolved_by.userprofile.district.name if obj.resolved_by.userprofile.district else "",
                "office_level": obj.resolved_by.userprofile.office_level.name if obj.resolved_by.userprofile.office_level else "",
            }
        return None