from django.db import models


# Create your models here.
class ToDo(models.Model):
  PRIORITY_TYPES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High')
  ]
  title = models.CharField(max_length = 128)
  priority = models.CharField(
    max_length = 1,
    choices = PRIORITY_TYPES)
  owner = models.CharField(max_length = 128)

  def __str__(self):
    return self.title
