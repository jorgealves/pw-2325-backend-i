from django.db import models


class UrlShort(models.Model):
    """
    This represents a URL shortened
    You must provide the following data:
    - source url
    - TTL (defaults to 86_400 seconds) 24h
    - shortened url (generated)
    """
    id=models.BigAutoField(primary_key=True)
    source_url=models.URLField(null=False,blank=False)
    ttl=models.BigIntegerField(default=86_400, null=False,blank=False)
    short_url=models.URLField(null=False,blank=False)

    class Meta:
        verbose_name="Shortened URL"
        verbose_name_plural="Shortened URLs"
