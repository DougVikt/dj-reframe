import sys
from pathlib import Path

__all__ = ["patch"]

_DJANGO_PATCHED = False


def patch():
    global _DJANGO_PATCHED
    if _DJANGO_PATCHED:
        return

    from dj_custom_starts.startapp import Command
    import django.core.management.commands.startapp as original

    original.Command = Command
    _DJANGO_PATCHED = True


def run():
    patch()
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)