from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ProductOrder


@receiver(post_save, sender=ProductOrder)
def update_on_save(sender, instance, created, **kwargs):
    """Update total_to_pay when a product update/create"""
    print(f'update_on_save is : {post_save}')
    instance.order.update_price()


@receiver(post_delete, sender=ProductOrder)
def update_on_delete(sender, instance, **kwargs):
    """Update total_to_pay when a product delete"""
    instance.order.update_price()
