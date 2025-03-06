from django.db import models

# class Todo(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
from django.db import models

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
