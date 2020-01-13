import uuid

import kwargs as kwargs
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Genre(models.Model):
    """Model representing a blog genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Tech)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Post(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular post")
    title = models.CharField(max_length=200, help_text='Enter the title of your post (e.g. My first Post)', unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this post')
    content = models.TextField(help_text='Write post content here!')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # def is_author(self):
    #     if self.Post.author == self.User:
    #         return True
    #     return False

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse('post-detail', args=[str(self.id)])


class PostInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular post")
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        db_index=0,
        help_text='Status of Posts'
    )

    class Meta:
        ordering = [Post.created_on],
        # permissions = (("can_create", "can_update", "can_delete"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.post.title)


