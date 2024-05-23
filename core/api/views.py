from rest_framework import generics
from .models import LeaveRequest, SiteIssue
from .serializers import LeaveRequestSerializer, SiteIssueSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class LeaveRequesListCreateAPIView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LeaveRequestSerializer

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(requested_by=user)

    def get_queryset(self):
        user = self.request.user
        if (
            user.userprofile.office_level.office_level == 1
            or user.userprofile.office_level.office_level == 2
        ):
            return LeaveRequest.objects.filter(requested_by=user).order_by(
                "-created_at"
            )
        else:
            return LeaveRequest.objects.filter(
                requested_by__userprofile__district__province=user.userprofile.district.province
            ).order_by("-created_at")

    # add can_approve on response
    def list(self, request, *args, **kwargs):
        response = super(LeaveRequesListCreateAPIView, self).list(
            request, *args, **kwargs
        )
        user = request.user
        if user.userprofile.office_level.office_level == 3:
            return Response({"data": response.data, "can_approve": True})
        else:
            return Response({"data": response.data, "can_approve": False})
        return response


class SiteIssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = SiteIssue.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SiteIssueSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(reported_by=user)

    def get_queryset(self):
        user = self.request.user
        # if user is on office lever 1 return only his/her requests
        if user.userprofile.office_level.office_level == 1:
            return SiteIssue.objects.filter(reported_by=user)
        # if user is on office lever 2 return all issues in his/her district that are open
        elif user.userprofile.office_level.office_level == 2:
            return SiteIssue.objects.filter(
                reported_by__userprofile__district=user.userprofile.district,
                status=SiteIssue.OPEN,
            ).order_by("-created_at")
        else:
            return SiteIssue.objects.filter(
                status=SiteIssue.TRANSFERED,
                reported_by__userprofile__district__province=user.userprofile.district.province,
            ).order_by("-created_at")

    # add can_resolve on response
    def list(self, request, *args, **kwargs):
        response = super(SiteIssueListCreateAPIView, self).list(
            request, *args, **kwargs
        )
        user = request.user
        if user.userprofile.office_level.office_level != 1:
            return Response({"data": response.data, "can_resolve": True})
        else:
            return Response({"data": response.data, "can_resolve": False})


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
