from django.db import models
from user.models import Profile


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    media_file = models.FileField(upload_to="files/")
    async_sending = models.BooleanField(null=False, blank=True)
    be_sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "پست ها"

    def __str__(self):
        return f"{self.id} - {self.title}"


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
