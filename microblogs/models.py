from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=30,
                                unique=True,
                                validators=[RegexValidator(
                                    regex=r'^@\w{3,}$',
                                    message='Username must consist of @ followed by at least three alphanumericals'
                                )]
                                )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=520, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=50, blank=True)
    text = models.CharField(max_length=280, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
