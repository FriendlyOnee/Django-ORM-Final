# Generated by Django 4.1.1 on 2022-10-08 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('post_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('post_rating', models.IntegerField(default=0)),
                ('comment_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('header', models.TextField(max_length=256)),
                ('date', models.DateField(auto_now_add=True)),
                ('restriction', models.CharField(choices=[('AR', 'Article'), ('NE', 'News'), ('EL', 'Else')], default='EL', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subhub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.subhub')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=models.SET('DELETED'), to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
    ]
