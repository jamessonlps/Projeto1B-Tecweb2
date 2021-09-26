from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return f'{self.title}'