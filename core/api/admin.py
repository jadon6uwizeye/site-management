from django.contrib import admin
from .models import LeaveRequest, SiteIssue

admin.site.register(LeaveRequest)
admin.site.register(SiteIssue)
