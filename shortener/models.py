from django.db import models
import string
import random
import uuid

class ShortenedLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(max_length=2000)
    shortened_link = models.CharField(max_length=8, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_used_date = models.DateTimeField(null=True, blank=True)
    use_count = models.PositiveIntegerField(default=0)
    referrer_url = models.URLField(max_length=2000, null=True, blank=True)
    cookies = models.TextField(null=True, blank=True)
    user_ip = models.GenericIPAddressField()
    user_agent = models.TextField()

    def save(self, *args, **kwargs):
        while not self.shortened_link:
            generated_link = self.generate_short_url()
            if not ShortenedLink.objects.filter(shortened_link=generated_link).exists():
                self.shortened_link = generated_link
        super().save(*args, **kwargs)

    @staticmethod
    def generate_short_url(length=8):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(length))
