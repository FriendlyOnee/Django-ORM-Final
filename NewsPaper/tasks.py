# Тут команды, которые нужно вставить, чтобы выполнить задания 9-11
from news.models import *

for user_i in UserProfile.objects.order_by("-post_rating"):
    print(user_i.user.username, user_i.post_rating, user_i.comment_rating)
    break

for post_i in Post.objects.order_by("-rating"):
    print(post_i.author.username, post_i.date, post_i.header, post_i.preview())
    for comment_i in Comment.objects.filter(pk=post_i.id):
        print(comment_i.date, comment_i.author.username, comment_i.rating, comment_i.content)
    break
