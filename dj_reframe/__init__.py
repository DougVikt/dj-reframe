from importlib.metadata import version, PackageNotFoundError

try:
    # O nome aqui DEVE ser o 'name' que está no seu pyproject.toml
    __version__ = version("dj-reframe")
except PackageNotFoundError:
    # Versão de fallback caso o pacote não esteja instalado
    __version__ = "0.0.0-dev"