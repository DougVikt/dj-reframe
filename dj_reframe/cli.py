import sys
import argparse
from pathlib import Path
import django
from django.conf import settings
from django.core.management import call_command
from dj_reframe import __version__


def main():
    # Cria o nosso próprio interpretador de terminal
    parser = argparse.ArgumentParser(description="Criador Avançado de Apps Django")
    
    parser.add_argument(
        "-V" , "--version",
        action = "version",
        version = f"%(prog)s {__version__}"
    )
    parser.add_argument("app_name", help="Nome do aplicativo (ex: blog, financeiro)")
    parser.add_argument("app_type", help="Tipo de arquitetura (ex: site, drf)")
    
    args = parser.parse_args()

    # Liga o motor do Django minimamente só para usar a função de gerar pastas
    if not settings.configured:
        settings.configure(INSTALLED_APPS=[])
        django.setup()

    # Descobre o caminho dos nossos arquivos -tpl
    base_dir = Path(__file__).resolve().parent
    template_path = base_dir / 'app_templates' / args.app_type

    if not template_path.exists():
        print(f"ERRO: Template '{args.app_type}' não encontrado!")
        print(f"   Procuramos em: {template_path}")
        sys.exit(1)

    try:
        # Usa o comando nativo do Django escondido!
        call_command('startapp', args.app_name, template=str(template_path))
        print(f"SUCESSO: App '{args.app_name}' (arquitetura '{args.app_type}') criado!")
    except Exception as e:
        print(f"ERRO do Django: {e}")

if __name__ == "__main__":
    main()