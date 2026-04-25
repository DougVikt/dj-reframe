from django.core.management.commands.startapp import Command


def patch():
    import django.core.management.commands.startapp as original

    original.Command = Command


import django.core.management

django.core.management.commands.startapp = __import__(
    "dj_custom_starts.startapp",
    fromlist=["Command"]
)