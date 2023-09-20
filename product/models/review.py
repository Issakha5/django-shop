from django.db import models
from django.contrib.auth.models import User
from ..models.product import Product


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
