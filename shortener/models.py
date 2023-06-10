import string
import random
import uuid

from django.db import models

class ShortenedLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(max_length=2000)  # Increase max_length if needed
    shortened_link = models.CharField(max_length=6, unique=True)  # The wyl.ink/<shortened_link>
    creation_date = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField()
    user_agent = models.TextField()  # user-agent can be quite long

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            self.shortened_link = self.generate_short_url()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_short_url(length=6):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(length))