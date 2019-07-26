from django.utils.text import slugify
import string
import rendom

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars)) for _ in range(size)


def unique_slug_generator(instance, new_slug=None):
	