from django.db import models
from user.models import Profile

# Create your models here.


class Message(models.Model):
    sender_message = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="sender_message"
    )
    receiver_message = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="receiver_message"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return f"sender = {self.sender_message}, reciver = {self.receiver_message}"
