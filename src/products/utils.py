import random
import string
# from .models import Product
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, newSlug=None):
    if not newSlug:
        slug = instance.title
    else:
        slug = newSlug
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exists()
    if qs:
        newSlug = "{slug}-{randomStr}".format(slug=slug, randomStr=random_string_generator(size=4))
        return unique_slug_generator(instance, newSlug=newSlug)
    else:
        return slug