from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # followed_by = models.ManyToManyField(
    #     "self", related_name="follow", symmetrical=False,null=True, blank=False
    # )

    personal_id = models.IntegerField(unique=True, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "کاربران"

    def __str__(self):
        return f"{self.id}"
