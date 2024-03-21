from django.db import models
from users.models import User
import uuid
# Create your models here.
class Ticket(models.Model):
    status_choices=(
        ('Active', 'Active'),
        ('Complete', 'Complete'),
        ('Pending', 'Pending')
    )
    type_choices = (
        ("Adult", "Adult"),
        ('Child', 'Child')
    )
    ticket_number = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="create_by")
    date_created = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_resolve = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)
    close_date = models.DateTimeField(null=True, blank=True)
    ticket_status = models.CharField(max_length=15, choices=status_choices)
    ticket_type = models.CharField(max_length=15, choices=type_choices)

    def __str__(self) -> str:
        return self.title