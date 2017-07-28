from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.name

class Author(models.Model):
    CA = 1
    DCA = 2
    TRAINER = 3
    CONTRIBUTOR = 4
    STATUS = (
        (CA, 'CA'),
        (DCA, 'DCA'),
        (TRAINER, 'Trainer'),
        (CONTRIBUTOR, 'Contributor'),
    )

    name = models.CharField(max_length = 150)
    description = models.TextField()
    # This is the name of the picture associated (without the extension)
    picture_handle = models.CharField(max_length = 50)
    status = models.IntegerField(default=3, choices = STATUS)
    def __unicode__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length = 30)
    # This is the name of the FontAwesome icon associated with the type
    picture_handle = models.CharField(max_length = 30)
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
    description = models.CharField(max_length = 350, default = '')
    authors = models.ManyToManyField(Author, blank = True)
    date_added = models.DateTimeField()
    content = models.TextField()
    category = models.IntegerField(choices = CATEGORY_CHOICES)
    tags = models.ManyToManyField(Tag)
    types = models.ManyToManyField(Type, blank = True)
    related_articles = models.ManyToManyField('self', symmetrical = False, blank = True)

    def __unicode__(self):
        return self.title

    