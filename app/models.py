from django.db import models

class News (models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self) -> str:
        return self.title