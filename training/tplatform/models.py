from django.db import models

class Article(models.Model):
    STRATEGY = 1
    CONTENT = 2
    MISC = 3
    CATEGORY_CHOICES = (
        (STRATEGY, 'Strategy'),
        (CONTENT, 'Content'),
        (MISC, 'Misc'),
    )

    title = models.CharField(max_length=200)
    # description = models.CharField(max_length=170)
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField()
    content = models.TextField()
    category = models.IntegerField(choices = CATEGORY_CHOICES)
    # TAGS_CHOICES = (
    #     (1, 'Tag1'),
    #     (2, 'Tag2'),
    #     (3, 'Tag3'),
    # )
    # tags = models.CharField(choices = TAGS_CHOICES)
