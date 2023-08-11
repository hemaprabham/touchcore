from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    text = models.TextField()

    def __str__(self):
        return f"{self.video.title} - {self.timestamp}: {self.text}"
