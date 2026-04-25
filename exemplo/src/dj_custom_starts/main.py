"""Entry point for dj_start command."""
import sys
from pathlib import Path


def run():
    package_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(package_dir))
    from dj_custom_starts import patch

    patch()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    run()