"""
Discuss Model Configuration
"""

from django.db import models

# Post model
class Posts(models.Model):
    content = models.TextField(max_length=500)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.content