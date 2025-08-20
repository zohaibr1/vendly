from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'
    
    def ready(self):
        # import signals so they register
        import customers.signals  # noqa: F401
