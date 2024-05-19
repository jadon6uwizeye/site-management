from django.urls import path
from .views import LeaveRequesListCreateAPIView, SiteIssueListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('leave/request/', LeaveRequesListCreateAPIView.as_view(), name='leave-request'),
    path('issues/', SiteIssueListCreateAPIView.as_view(), name='leave-request-detail'),
]