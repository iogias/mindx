from django.db import models
from django.utils import timezone


class UnityEmail(models.Model):
    SUBS = [
        ('subs', 'Subscribed'),
        ('unsubs', 'Unsubscribed'),
    ]
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=6, choices=SUBS, default='subs')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return f"{self.email}"
