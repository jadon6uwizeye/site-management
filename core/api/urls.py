from django.urls import path
from .views import LeaveRequesCreateAPIView, SiteIssueCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('leave/request/', LeaveRequesCreateAPIView.as_view(), name='leave-request'),
    path('leave/request/<int:pk>/', SiteIssueCreateAPIView.as_view(), name='leave-request-detail'),
]