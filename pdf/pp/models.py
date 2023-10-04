from django.db import models

# Create your models here.

class pdfs(models.Model):
    title=models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
