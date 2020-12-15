from django.db import models

# Create your models here.

FOOD_CHOICES = (
    ('orange', 'orange'),
    ('pineapple', 'pineapple'),
    ('juice', 'juice'),
)


class FooditemsModel(models.Model):
    itemname = models.CharField(max_length=20, choices=FOOD_CHOICES, default='empty')
    table_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.table_id