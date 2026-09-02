from django.db import models



class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField()

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} - {self.company}"
    


