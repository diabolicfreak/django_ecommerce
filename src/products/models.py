from django.db import models
from django.urls import reverse
import os
import random
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    filename, ext = os.path.splitext(basename)
    return filename, ext

def handle_file_upload(instance, filepath):
    new_filename = random.randint(0, 33647433)
    name, ext = get_filename_ext(filepath)
    final_filepath = "{new_filename}/{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return final_filepath

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to=handle_file_upload, null=True, blank=True)
    featured = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)