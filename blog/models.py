# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    sort_asc = models.BooleanField(default=False)
    grop_0 = models.BooleanField(default=True)
    grop_1 = models.BooleanField(default=False)
    grop_2 = models.BooleanField(default=False)
    grop_3 = models.BooleanField(default=False)
    grop_4 = models.BooleanField(default=False)
    grop_5 = models.BooleanField(default=False)

#    list_display = ('title', 'text')
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('tekst', {'fields': ['title'] }),
    ]
    inlines = [grop_0, grop_1, grop_2, grop_3, grop_4, grop_5]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def delete_comments(self):
        return True

    def filter_group(self, number):
        if number == 1 and self.grop_1 == True:
            return True
        elif number == 2 and self.grop_2 == True:
            return True
        elif number == 3 and self.grop_3 == True:
            return True
        elif number == 4 and self.grop_4 == True:
            return True
        elif number == 5 and self.grop_5 == True:
            return True
        elif number == 0 and self.grop_0 == True:
            return True

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('auth.User') # models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def __unicode__(self):
        return u'%s' % self.text

class Document(models.Model):
    post = models.ForeignKey('blog.Post', related_name='documents')
    #docfile = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
    docfile = models.ImageField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='documents/%Y/%m/%d/thumbs', null=True, blank=True, editable=False)
    title = models.CharField(max_length=255, null=True)
    #created_date = models.DateTimeField(default = timezone.now)
    #updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"id": self.id})

    def url(self):
        self.docfile.storage()

    def delete(self, *args, **kwargs):
        storage, path = self.docfile.storage, self.docfile.path
        storaget, patht = self.thumbnail.storage, self.thumbnail.path
        super(Document, self).delete()
        storage.delete(path)
        storaget.delete(patht)

    def createThumbnail(self):
        if not self.docfile:
            return
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os
        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (200,200)
        DJANGO_TYPE = self.docfile.file.content_type
        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        image = Image.open(StringIO(self.docfile.read()))
        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.docfile.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

    def save(self):
        # create a thumbnail
        self.createThumbnail()

        super(Document, self).save()
