from django.db import models
import os
import random

def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    filename, ext = os.path.splitext(basename)
    return filename, ext

def handle_file_upload(instance, filepath):
    new_filename = random.randint(0, 33647433)
    name, ext = get_filename_ext(filepath)
    final_filepath = "{new_filename}/{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return final_filepath

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to=handle_file_upload, null=True, blank=True)

    def __str__(self):
        return self.title