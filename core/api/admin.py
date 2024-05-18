from django.contrib import admin
from .models import LeaveRequest, SiteIssue

# change Django admin headers and names
admin.site.site_header = 'Sites Administration'
admin.site.site_title = 'Sites administration'

admin.site.register(LeaveRequest)
admin.site.register(SiteIssue)
