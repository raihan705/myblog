from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# from application import


#custom manager creation:

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
        .filter(status='published')




# Create your models here.


class Post(models.Model):

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    postimage = models.ImageField(null=True, blank=True,upload_to = 'images/')
    body = models.TextField()
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
        args=[self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug])
    



