from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class EdghamPage(models.Model):
    store = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_edghamPage')
    page_link = models.URLField(max_length=400)
    product_name = models.CharField(max_length=256)
    prev_fisrt_product_price = models.FloatField(null=True, blank=True)
    fisrt_product_price = models.FloatField(null=True, blank=True)
    prev_second_product_price = models.FloatField(null=True, blank=True)
    second_product_price = models.FloatField(null=True, blank=True)
    prev_my_product_price = models.FloatField(null=True, blank=True)
    my_product_price = models.FloatField(null=True, blank=True)
    prev_my_product_rank = models.IntegerField(null=True, blank=True)
    my_product_rank = models.IntegerField(null=True, blank=True)
    is_your_product_on_this_page = models.BooleanField(default=False)

    created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.store.username} ---------> {self.product_name}'
