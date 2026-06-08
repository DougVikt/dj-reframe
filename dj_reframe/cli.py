import argparse
import django
import os
import platform
import subprocess
import sys
from dj_reframe import __version__
from django.conf import settings
from django.core.management import call_command
from pathlib import Path



"""
 Sets the folder in the user's "Home" directory to store custom templates.
 E.g.,C:/Users/Name/.dj-reframe/my_templates on Windows,
 or ~/.dj-reframe/my_templates on Linux/Mac
"""
USER_HOME_DIR = Path.home() / ".dj-reframe" / "my_templates"


def open_file_explorer(path: Path) -> None:
    """
    Opens the operating system's file manager in the specified folder.
    If the folder does not exist, it will be created
    """
    path.mkdir(parents=True, exist_ok=True)
    print(f"📂 Opening the user's template folder: {path}")
    # Check the operating system to run the correct command to open the folder visually
    current_os = platform.system()
    if current_os == "Windows":
        # os.startfile only exists on Windows
        if hasattr(os, "startfile"):
            os.startfile(path)
    elif current_os == "Darwin":
        # For macOS
        subprocess.Popen(["open", path])
    else:
        # For Linux
        subprocess.Popen(["xdg-open", path])


def main() -> None:
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(
        description="""Advanced Django app creator with
        customizable architecture templates"""
    )
    # Argument to display version
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"dj-reframe {__version__}",
        help="Show the installed version",
    )
    '''
    Positional arguments (app name and architecture type).
    They are set as OPTIONAL (nargs='?') to allow the '--my-templates'
    flag to work on its own.
    '''
    parser.add_argument("app_name", nargs="?", help="Application name (e.g., blog)")
    parser.add_argument(
        "app_type", nargs="?", help="Architecture type (e.g., site, drf)"
    )

    # Optional argument (flag) to open the user's custom templates folder
    parser.add_argument(
        "--my-templates",
        action="store_true",
        help="Opens the folder for you to add your own templates",
    )

    # Parse the arguments entered by the user in the terminal
    args = parser.parse_args()

    # Flow 1: If the user passed the --my-templates flag,
    # open the folder and exit the script (sys.exit(0) = success)
    if args.my_templates:
        open_file_explorer(USER_HOME_DIR)
        sys.exit(0)

    # Flow 2: If the open folder flag was not passed,
    # ensure both app name and app type are provided
    if not args.app_name or not args.app_type:
        parser.print_help()
        sys.exit(1)

    # Django Validation: Check if the app name contains a hyphen,
    # which is not allowed in Python modules
    if "-" in args.app_name:
        print(
            """❌ERROR:Django does not accept hyphens '-' in the app name.
            \n Use underscores '_'."""
        )
        sys.exit(1)

    '''
    Minimal Django Configuration (Standalone mode)
    Required so Django allows running management commands (like 'startapp')
    without a manage.py file
    '''
    if not settings.configured:
        settings.configure(INSTALLED_APPS=[])
        django.setup()

    # Define paths for user custom templates and package default templates
    user_template_path = USER_HOME_DIR / args.app_type
    package_template_path = (
        Path(__file__).resolve().parent / "app_templates" / args.app_type
    )

    # Priority: use user template if it exists, otherwise fall back to package template
    if user_template_path.exists():
        template_path = user_template_path
        print(f"💡 Using user template: {args.app_type}")
    elif package_template_path.exists():
        template_path = package_template_path
    else:
        # No template found in either location
        print(f"❌ ERROR: Template '{args.app_type}' not found!")
        print("   Tip: Create yours by typing 'dj-reframe --my-templates'")
        sys.exit(1)

    # Attempt to create the Django app using the resolved template
    try:
        call_command("startapp", args.app_name, template=str(template_path))
        print(
            f"✨SUCCESS:App '{args.app_name}' (architecture '{args.app_type}')created"
        )
    except Exception as e:
        # Catch and display any Django-related errors during app creation
        print(f"❌ Django ERROR: {e}")


if __name__ == "__main__":
    main()
