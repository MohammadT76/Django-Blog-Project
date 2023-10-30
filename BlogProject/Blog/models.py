from django.db                  import models
from django.utils               import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title   = models.CharField(max_length=300)
    slug    = models.SlugField(max_length=300,
                               help_text='Slug is a field in autocomplete mode, but if you want you can modify its contents',
                               verbose_name='Slug',unique=True)
    body    = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # for more information about `one_delete` parameter , you can see the following link:
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey.on_delete
    author  = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts')

    # A common functionality for blogs is to save posts as a draft until ready for publication. 
    # The available choices for the post status are : 1) draft 2) published --> Post.Status.names
    # Their respective values are                   : 1) DF    2) PB        --> Post.Status.values
    # Their labels or readable names are            : 1) Draft 2) Published --> Post.Status.labels
    class Status(models.TextChoices):
        draft     = 'DF' , 'Draft'
        published = 'PB' , 'Published'

    status  = models.CharField(max_length=2,choices=Status.choices,default=Status.draft)

    class Meta:
        ordering = ['-publish']

        # This will improve performance for queries filtering or ordering results by these fields.
        indexes = [
            models.Index(fields=['-publish'])
        ]

        db_table_comment = "User posts"
        # if you want changing the default table names , you can uncomment the following line.
        # db_table = "post_model"

    # when you call an object from this class , object's title shows
    def __str__(self):
        return self.title

