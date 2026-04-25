#!/usr/bin/env python
import sys
from pathlib import Path

DJANGO_PATCH_FILE = Path(__file__).parent / "dj_patch.py"


def main():
    sys.path.insert(0, str(Path(__file__).parent))

    from dj_custom_starts.monkey import patch

    patch()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()