from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    birthdate = models.DateField(null=True, blank=True)
    post_rating = models.IntegerField(default=0)
    comment_rating = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    def update_post_rating(self):
        self.post_rating = self.rating_calc('Post')
        self.save()

    def update_comment_rating(self):
        self.comment_rating = self.rating_calc('Comment')
        self.save()

    def rating_calc(self, type_for_update):
        if type_for_update == 'Comment':
            related_comments = Comment.objects.filter(author=self.user)
            rating = list(related_comments.values_list('rating', flat=True))
            return sum(rating)
        else:
            related_posts = Post.objects.filter(author=self.user)
            rating = list(related_posts.values_list('rating', flat=True))
            return sum(rating)

    def __str__(self):
        return self.user.username


# У меня такая альтернатива категориям, каждый сможет создавать саб хаб, в одном саб хабе может быть много постов
class SubHub(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=256)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}: {self.description[0:64]}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subhub = models.ForeignKey(SubHub, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    content = models.TextField(max_length=1024)
    header = models.TextField(max_length=128)
    date = models.DateField(auto_now_add=True)
    ARTICLE = "AR"
    NEWS = "NE"
    ELSE = "EL"
    RESTRICTION_CHOICES = [
        (ARTICLE, "Article"),
        (NEWS, "News"),
        (ELSE, "Else")
    ]
    restriction = models.CharField(
        max_length=2,
        choices=RESTRICTION_CHOICES,
        default=ELSE
    )

    def preview(self):
        if len(self.content) >= 64:
            return f'{self.content[0:64]}...'
        else:
            return self.content

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_rating(self):
        return self.rating

    def __str__(self):
        return f'{self.header}: {self.content[0:64]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET('DELETED'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    content = models.TextField(max_length=1024)
    date = models.DateField(auto_now_add=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_rating(self):
        return self.rating

    def __str__(self):
        return f'{self.post}: {self.content[0:64]}'
# Create your models here.
