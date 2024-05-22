from rest_framework import generics
from .models import LeaveRequest, SiteIssue
from .serializers import LeaveRequestSerializer, SiteIssueSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

class LeaveRequesListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LeaveRequestSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        print("user", user)
        serializer.save(requested_by=user)
        
    # if admin user, return all leave requests else return only the user's leave requests
    # add aprove boolean field to the serializer
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return LeaveRequest.objects.all()
        return LeaveRequest.objects.filter(requested_by=user)
    
    def get_serializer_context(self):
        context = super(LeaveRequesListCreateAPIView, self).get_serializer_context()
        context.update({"user": self.request.user})
        return context

class SiteIssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = SiteIssue.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SiteIssueSerializer
    
    def perform_create(self, serializer):
        user = get_user_model().objects.all().first()
        print("user", user)
        serializer.save(reported_by=user)
        
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return SiteIssue.objects.all()
        return SiteIssue.objects.filter(reported_by=user)
    
    def get_serializer_context(self):
        context = super(SiteIssueListCreateAPIView, self).get_serializer_context()
        context.update({"user": self.request.user})
        return context
    
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def transfer_issue(request, issue_id):
    try:
        issue = SiteIssue.objects.get(id=issue_id)
        issue.transfered = True
        issue.transferred_by = request.user
        issue.status = SiteIssue.TRANSFERED
        issue.save()
        return Response({"message": "Issue Transferred successfully"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def resolve_issue(request, issue_id):
    try:
        issue = SiteIssue.objects.get(id=issue_id)
        issue.status = SiteIssue.RESOLVED
        issue.resolved_by = request.user
        issue.save()
        return Response({"message": "Issue Resolved successfully"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def approve_request(request, request_id):
    try:
        leave_request = LeaveRequest.objects.get(id=request_id)
        leave_request.status = LeaveRequest.APPROVED
        leave_request.approved_by = request.user
        leave_request.save()
        return Response({"message": "Request Approved successfully"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_request(request, request_id):
    try:
        leave_request = LeaveRequest.objects.get(id=request_id)
        leave_request.delete()
        return Response({"message": "Request Deleted successfully"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_issue(request, issue_id):
    try:
        issue = SiteIssue.objects.get(id=issue_id)
        issue.delete()
        return Response({"message": "Issue Deleted successfully"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)