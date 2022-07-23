from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='portfolio/media/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title#Makes the title of project to display in admin page
