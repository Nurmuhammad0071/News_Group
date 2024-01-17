from django.db import models


# Create your models here.
class News(models.Model):
    STATUS = (
        ('active', "Active"),
        ('noactive', "NoActive")
    )
    title = models.CharField(max_length=250)
    text = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Yangliklar"

    def __str__(self):
        return self.title

    object = models.Manager()


posts = News.object.filter(status="active")
