from django.db import models


class Service(models.Model):
    ICON_CHOICES = (
        ('twf-cleaning-1', 'twf-cleaning-1'),
        ('twf-cleaning-2', 'twf-cleaning-2'),
        ('twf-cleaning-3', 'twf-cleaning-3'),
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    min_value = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    quantity_hours = models.IntegerField(null=False, blank=False)
    commission_percentage = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    bedroom_hours = models.IntegerField(null=False, blank=False)
    bedroom_value = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    living_room_hours = models.IntegerField(null=False, blank=False)
    living_room_value = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    bathroom_hours = models.IntegerField(null=False, blank=False)
    bathroom_value = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    kitchen_hours = models.IntegerField(null=False, blank=False)
    kitchen_value = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    backyard_hours = models.IntegerField(null=False, blank=False)
    backyard_value = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    other_hours = models.IntegerField(null=False, blank=False)
    other_value = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    icon = models.CharField(max_length=14, null=False, blank=False, choices=ICON_CHOICES)
    position = models.IntegerField(null=False)
