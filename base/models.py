from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="images", storage=FileSystemStorage("base/static"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    text = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created = models.DateField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.text}"

