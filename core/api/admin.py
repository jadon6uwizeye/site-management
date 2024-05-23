from django.contrib import admin
from .models import LeaveRequest, SiteIssue, OfficeLevel, District, userProfile, Province

# change Django admin headers and names
admin.site.site_header = 'Sites Administration'
admin.site.site_title = 'Sites administration'

class OfficeLevelAdmin(admin.ModelAdmin):
    list_display = ('office_level', 'name')
    search_fields = ('office_level', 'name')
    list_filter = ('office_level', 'name')
    ordering = ('office_level', 'name')
    
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')
    search_fields = ('name', 'province')
    list_filter = ('name', 'province')
    ordering = ('name', 'province')
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'district', 'office_level')
    search_fields = ('user', 'district', 'office_level')
    list_filter = ('user', 'district', 'office_level')
    ordering = ('user', 'district', 'office_level')
    
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'leave_type', 'start_date', 'end_date', 'status')
    search_fields = ('requested_by', 'leave_type', 'start_date', 'end_date', 'status')
    list_filter = ('requested_by', 'leave_type', 'start_date', 'end_date', 'status')
    ordering = ('requested_by', 'leave_type', 'start_date', 'end_date', 'status')
    

admin.site.register(LeaveRequest, LeaveRequestAdmin)
admin.site.register(SiteIssue)
admin.site.register(OfficeLevel, OfficeLevelAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(userProfile, UserProfileAdmin)
admin.site.register(Province)
