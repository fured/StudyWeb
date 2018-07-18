# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from .timestamp import UnixTimestampField

class BookTable(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    author_contry = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    book_image_path = models.CharField(max_length=100)
    book_download_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'book_table'


class CommentTable(models.Model):
    comment_name = models.CharField(max_length=50)
    comment_email = models.CharField(max_length=50)
    comment_message = models.CharField(max_length=500)
    create_at = models.FloatField()

    class Meta:
        managed = False
        db_table = 'comment_table'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'

class CommentMovieTable(models.Model):
    user_name = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    user_img_path = models.CharField(max_length=100)
    user_address = models.CharField(max_length=100)
    BeReplyName = models.CharField(max_length=50)
    OSName = models.CharField(max_length=50)
    BrowerName = models.CharField(max_length=50)
    ReplyBody = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "comment_movie_table"


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class PlayMusicTable(models.Model):
    song_name = models.CharField(max_length=50)
    songer_name = models.CharField(max_length=50)
    song_image_path = models.CharField(max_length=100)
    song_type = models.CharField(max_length=100)
    storage_path = models.CharField(max_length=100)
    createdTime = UnixTimestampField()
    class Meta:
        managed = False
        db_table = 'play_music_table'


class UserTable(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
#    createdTime = UnixTimestampField()
    class Meta:
        managed = False
        db_table = 'user_table'


class RecommendMusicTable(models.Model):
    song_name = models.CharField(max_length=50)
    song_type = models.CharField(max_length=50)
    recommend_name = models.CharField(max_length=50)
    recommend_reason = models.CharField(max_length=500)
    create_at = models.FloatField()

    class Meta:
        managed = False
        db_table = 'recommend_music_table'


class ShareMoiveTable(models.Model):
    moive_name = models.CharField(max_length=50)
    share_reason = models.CharField(max_length=500)
    moive_image_path = models.CharField(max_length=100)
    moive_download_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'share_moive_table'
