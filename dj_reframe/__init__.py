from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("dj-reframe")
except PackageNotFoundError:
    __version__ = "0.0.0"
