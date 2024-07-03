from django.db import models

class TravelOrdersStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    CONFIRMED = 'COMFIRMED', 'Confired'
    SHIPPED = 'SHIPPED', 'Shipped'
    DELIVERED = 'DELIVERED', 'Delivered'
    CANCELLED = 'CANCELLED', 'Cancelled'