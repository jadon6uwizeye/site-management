from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Province(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Cell(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class OfficeLevel(models.Model):
    office_level = models.IntegerField()
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    office_level = models.ForeignKey(OfficeLevel, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
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
    
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approved_by", null=True, blank=True)
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
        return f"{self.requested_by} - {self.leave_type}"

class SiteIssue(models.Model):
    # status choices
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    TRANSFERED = "Transfered"
    STATUS_CHOICES = [
        (OPEN, "Open"),
        (IN_PROGRESS, "In Progress"),
        (RESOLVED, "Resolved"),
        (TRANSFERED, "Transfered"),
    ]
    
    issue_title = models.CharField(max_length=50)
    issue_description = models.TextField(null=True, blank=True)
    supporting_document = models.FileField(upload_to="supporting_documents/")
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    transfered = models.BooleanField(default=False)
    transferred_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transferred_by", null=True, blank=True)
    resolved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resolved_by", null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.issue_title
    
    class Meta:
        verbose_name_plural = "Site Issues"