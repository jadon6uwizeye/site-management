from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class LeaveRequest(models.Model):
    # leave_type choices
    CASUAL_LEAVE = "Casual Leave"
    SICK_LEAVE = "Sick Leave"
    VACATION_LEAVE = "Vacation Leave"
    MATERNITY_LEAVE = "Maternity Leave"
    PATERNITY_LEAVE = "Paternity Leave"
    UNPAID_LEAVE = "Unpaid Leave"
    LEAVE_TYPE_CHOICES = [
        (CASUAL_LEAVE, "Casual Leave"),
        (SICK_LEAVE, "Sick Leave"),
        (VACATION_LEAVE, "Vacation Leave"),
        (MATERNITY_LEAVE, "Maternity Leave"),
        (PATERNITY_LEAVE, "Paternity Leave"),
        (UNPAID_LEAVE, "Unpaid Leave"),
    ]
    
    # status choices
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected"),
    ]
    
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(
        max_length=50, choices=LEAVE_TYPE_CHOICES, default=CASUAL_LEAVE
    )
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    supporting_document = models.FileField(upload_to="supporting_documents/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_id


class SiteIssue(models.Model):
    # status choices
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    STATUS_CHOICES = [
        (OPEN, "Open"),
        (IN_PROGRESS, "In Progress"),
        (RESOLVED, "Resolved"),
    ]
    
    issue_title = models.CharField(max_length=50)
    issue_description = models.TextField(null=True, blank=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.issue_title
    
    class Meta:
        verbose_name_plural = "Site Issues"