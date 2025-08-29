from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_profile(sender, instance, created, **kwargs):
    role = getattr(instance, "role", None)
    if created and role and role.upper() == "CUSTOMER":
        from .models import CustomerProfile
        CustomerProfile.objects.create(user=instance)
