#!/usr/bin/env python
"""Wrapper that patches Django before loading."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from dj_custom_starts import patch

patch()

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)