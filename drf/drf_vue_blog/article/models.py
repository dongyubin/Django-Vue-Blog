from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  created = models.DateTimeField(default=timezone.now)
  updated = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(
    User, 
    null=True,
    on_delete=models.CASCADE, 
    related_name='articles'
  )
  def __str__(self) -> str:
    return self.title