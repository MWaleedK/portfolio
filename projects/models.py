from django.db import models

class Project(models.Model):


    title = models.CharField(max_length=200)

    description = models.TextField()

    technologies = models.CharField(max_length=500)

    github_url = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)

    project_url = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def technology_list(self):
        return [
            technology.strip()
            for technology in self.technologies.split(",")
            if technology.strip()
        ]

    def __str__(self):
        return self.title

