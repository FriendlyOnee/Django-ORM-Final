# Тут команды, которые нужно вставить, чтобы выполнить задания 9-11
from news.models import *

UserProfile.objects.order_by("-post_rating")

UserProfile.objects.get(pk=1).date_joined

for e in Post.objects.filter(author=UserProfile.objects.get(pk=1).user):
    print(e.header, e.preview(), e.rating)
