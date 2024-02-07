from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    date = models.DateField()
    status = models.BooleanField(default=False)
    # new_slug = AutoSlugField()

    def __str__(self):
        return self.todo_name