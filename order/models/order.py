from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    ORDERED = "ordered"
    SHIPPED = "shipped"

    STATUS_CHOICES = ((ORDERED, "Ordered"), (SHIPPED, "Shipped"))

    user = models.ForeignKey(
        User, related_name="orders", blank=True, null=True, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    zipcode = models.CharField(max_length=70)
    place = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ("-created_at",)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount / 100

        return 0
