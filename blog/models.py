from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/media/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class BlogProject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    #to make these appear in admin page do register this class in admin.py

    def __str__(self):
        return self.name
