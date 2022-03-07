from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.


class FileModels( models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='file_customer')
    files = models.FileField( upload_to="media/%Y%m%d/", null=True, blank=True)
    created = models.DateTimeField( auto_now_add=True)

    class Meta():
        ordering = ['-created', '-user']

    def __str__(self):
        return "{}-{}".format( self.user, self.files)


class MoTestModel( models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
    father = models.CharField( max_length=200, blank=True)
    mother = models.CharField( max_length=200, blank=True)
    baby = models.CharField( max_length=200, blank=True)

    email = models.EmailField( max_length=200, blank=True)
    phone = models.CharField( max_length=200, blank=True)

    event_date = models.DateTimeField( null=True, blank=True)

    photo_first = models.ManyToManyField( FileModels, related_name="photo_first", blank=True)
    content_first = models.CharField( max_length=200, blank=True)

    photo_sec = models.ManyToManyField( FileModels, related_name="photo_sec", blank=True)
    content_sec = models.CharField( max_length=200, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, null=True, blank=True)

    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)

    class Meta():
        ordering = ['-created', '-user']

    def __str__(self):
        return "{}-{}".format( self.user, self.created)

    def get_absolute_url(self):
        return reverse('motest:motest_detail', kwargs={'pk': self.id})
