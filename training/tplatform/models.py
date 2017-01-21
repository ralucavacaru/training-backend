from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.name

class Article(models.Model):
    STRATEGY = 1
    CONTENT = 2
    MISC = 3
    CATEGORY_CHOICES = (
        (STRATEGY, 'Strategy'),
        (CONTENT, 'Content'),
        (MISC, 'Misc'),
    )

    title = models.CharField(max_length = 200)
    # description = models.CharField(max_length=170)
    author = models.CharField(max_length = 50)
    date_added = models.DateTimeField()
    content = models.TextField()
    category = models.IntegerField(choices = CATEGORY_CHOICES)
    tags = models.ManyToManyField(Tag)