from django.db import models

# Create your models here.


class Task(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
