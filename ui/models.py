from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100, default='#')
    image = models.ImageField(default='default.jpg', upload_to='project_images')
    technology = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email
