from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        """_summary_
        To specify a table name instead of using the default name generated 
        by Django, you can use the db_table attribute of the Meta class
        """
        # db_table = "posts"
        ordering = ["-published_at"]
