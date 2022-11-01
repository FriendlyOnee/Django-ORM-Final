from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    birthdate = models.DateField(null=True, blank=True)
    post_rating = models.IntegerField(default=0)
    comment_rating = models.IntegerField(default=0)

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


# У меня такая альтернатива категориям, каждый сможет создавать саб хаб, в одном саб хабе может быть много постов
class SubHub(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=256)
    post_count = models.IntegerField(default=0)


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
        return self.content[0:128]

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_rating(self):
        return self.rating


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
# Create your models here.
