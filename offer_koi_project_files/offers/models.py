from django.db import models
from django.utils import timezone

class Offers(models.Model):
    DISCOUNT_CHOICE = (
        (False, 'Flat'),
        (True, 'Percentage')
    )

    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to='upload/', blank=True)

    # dicount type => flat = 0 and percentage = 1
    discount_type = models.BooleanField(default=False, choices=DISCOUNT_CHOICE)
    discount_amount = models.IntegerField(default=None)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    shop_id = models.IntegerField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
