"""Custom Django startapp command with templates and extras."""

import shutil
from pathlib import Path
from django.core.management.commands.startapp import Command as BaseCommand


def patch():
    import django.core.management.commands.startapp as original

    original.Command = Command


class Command(BaseCommand):
    help = "Creates a custom Django app with optional extras."

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--extras",
            action="store_true",
            default=False,
            help="Include extra files (urls, services, permissions).",
        )
        parser.add_argument(
            "--api",
            action="store_true",
            default=False,
            help="Create API-ready app structure (DRF serializers, viewsets).",
        )

    def handle(self, **options):
        self.extras = options.get("extras", False)
        self.is_api = options.get("api", False)
        super().handle(**options)

        app_name = options["name"]
        target = options.get("target")
        app_path = Path(target or ".") / app_name if target else Path.cwd() / app_name

        if self.extras or self.is_api:
            self._create_extra_files(app_name, app_path)

        self.stdout.write(self.style.SUCCESS(f"App '{app_name}' created successfully!"))

    def _create_extra_files(self, app_name, app_path):
        if self.is_api:
            self._create_api_structure(app_name, app_path)
        else:
            self._create_basic_extras(app_name, app_path)

    def _create_basic_extras(self, app_name, app_path):
        files = {
            "urls.py": f"""from django.urls import path

app_name = "{app_name}"

urlpatterns = [
    # path('', views., name=''),
]
""",
            "services.py": "# Services layer\n",
            "permissions.py": "# Custom permissions\n",
        }
        for filename, content in files.items():
            (app_path / filename).write_text(content)

    def _create_api_structure(self, app_name, app_path):
        files = {
            "serializers.py": f"""from rest_framework import serializers

# {app_name} Serializers
""",
            "urls_api.py": f"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"", views.ModelViewSet, basename="{app_name}")

app_name = "{app_name}"

urlpatterns = [
    path("api/", include(router.urls)),
]
""",
            "views.py": f"""from rest_framework import viewsets

class ModelViewSet(viewsets.ModelViewSet):
    pass
""",
        }
        for filename, content in files.items():
            (app_path / filename).write_text(content)


patch()