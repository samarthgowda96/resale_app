from django.db import models
import uuid
import datetime
import os
# Create your models here.
def filepath(request, filename): # File Path for your uploaded media
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s_%s' % (timeNow, old_filename)
    return os.path.join('media/', filename)
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    name = models.CharField(max_length=512)
    location = models.CharField(null=True, max_length=512)
    email = models.EmailField(null=True)
    phone_no = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.name
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    book_name = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    book_image = models.FileField(upload_to=filepath, unique=True)
class BookUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=512)
class CommentUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)