from django.contrib.auth.models import User
user = User.objects.last()
post1 = Post.objects.create(author_id
