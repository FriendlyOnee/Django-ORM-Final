from django.contrib.auth.models import User
user = User.objects.last()
post1 = Post.objects.create(author_id
for post_i in Post.objects.order_by("-rating"):
    print(post_i.author.username, post_i.date, post_i.header, post_i.preview())
    print(Comment.objects.filter(post_i))
    for comment_i in Comment.objects.filter(post_i):
        print(comment_i.date, comment_i.rating, comment_i.content)
    break