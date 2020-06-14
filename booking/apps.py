from django.apps import AppConfig


class BookingConfig(AppConfig):
    name = 'booking'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import booking.signals
