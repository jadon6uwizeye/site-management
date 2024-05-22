from django.urls import path
from .views import (
    LeaveRequesListCreateAPIView,
    SiteIssueListCreateAPIView,
    transfer_issue,
    approve_request,
    delete_request,
    delete_issue,
    resolve_issue,
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path(
        "leave/request/", LeaveRequesListCreateAPIView.as_view(), name="leave-request"
    ),
    path("issues/", SiteIssueListCreateAPIView.as_view(), name="leave-request-detail"),
    path("issues/transfer/<int:issue_id>/", transfer_issue, name="transfer-issue"),
    path("leave/approve/<int:request_id>/", approve_request, name="approve-request"),
    path("leave/delete/<int:request_id>/", delete_request, name="delete-request"),
    path("issues/delete/<int:issue_id>/", delete_issue, name="delete-issue"),
    path("issues/resolve/<int:issue_id>/", resolve_issue, name="resolve-issue"),
]
