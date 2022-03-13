from django.db import models

from authentication.models import User
# # ALternative way of importing User model
# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your models here.
class Order(models.Model):
    MOMO_SIZES = (
        ('SMALL','Small'),
        ('MEDIUM','Medium'),
        ('LARGE','Large'),
    )

    ORDER_STATUSES = (
        ('PENDING','Pending'),
        ('IN_TRANSIT','In_Transit'),
        ('DELIVERED','delivered')
    )

    order_status = models.CharField(max_length=25, choices = ORDER_STATUSES, default= ORDER_STATUSES[0][0])
    size = models.CharField(max_length=25, choices = MOMO_SIZES, default= MOMO_SIZES[0][0])
    plate_quantity = models.IntegerField()
    flavour = models.CharField(max_length=40)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Order {self.flavour} by {self.customer}>"



