# dj-reframe

Advanced Django App Creator with customizable architecture templates.

## Description

DjReframe is a Django extension that transforms the standard `startapp` command. Instead of a generic default structure, DjReframe lets you create applications with specialized architectures (Web, API/DRF, Service Layer, etc.) in seconds. You can use our predefined structures or create your own.

## Features

- 🚀 **Multiple Architecture Templates**: Create Django apps with pre-defined architectures
- 🎨 **Custom Templates**: Use your own templates by adding them to your user folder
- 📁 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🔧 **CLI Interface**: Simple command-line interface with clear feedback
- ✅ **Django Validation**: Validates app names and prevents common mistakes

## Installation

```bash
pip install dj-reframe
```

Or with Poetry:

```bash
poetry add dj-reframe
```

## Upgrade

Keep your package up to date with the latest updates

```bash
pip install --upgrade dj-reframe
```

## Usage

### Basic Usage

Create a new Django app with a specific architecture:

```bash
dj-reframe <app_name> <architecture_type>
```

Examples:

```bash
# Create a web app
dj-reframe blog sitev1

# Create a DRF API app
dj-reframe api drf

# Create a WebSocket app
dj-reframe chat websockets
```

### Using Custom Templates

You can create your own templates and use them with DjReframe:

```bash
# Open the custom templates folder
dj-reframe --my-templates
```

This will open the folder where you can add your own architecture templates. Just create a new folder with your template name and add your Django app structure inside it.

#### 📝 Template File Naming Rules

For DjReframe (and Django's `startapp`) to recognize and properly process your custom templates, **all Python files must end with `.py-tpl`** instead of `.py`.

**Why?** When Django creates an app from a template, it automatically strips the `-tpl` suffix. So `views.py-tpl` becomes `views.py` in the generated app.

**Example of a custom template structure:**
```
my-custom-arch/
├── __init__.py-tpl
├── admin.py-tpl
├── apps.py-tpl
├── models.py-tpl
├── views.py-tpl
├── urls.py-tpl
├── migrations/
│   └── __init__.py-tpl
├── static/
│   └── app_name/
└── templates/
    └── app_name/
```

**Important:**
- ✅ Python files: MUST use `.py-tpl` (e.g., `models.py-tpl`)
- ✅ Non-Python files: Use normal extensions (e.g., `style.css`, `index.html`)
- ✅ Directories: No special suffix needed (e.g., `migrations/`, `templates/`)

Once your template is ready, use it with:
```bash
dj-reframe <app_name> my-custom-arch
```

### Available Architectures

Click on each architecture to see its complete structure:

<details>
<summary><b>sitev1</b> - Basic Django web application</summary>

```
sitev1/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── urls.py
├── views.py
├── migrations/
│   └── __init__.py
├── static/
│   └── app_name/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
└── templates/
    └── app_name/
        └── index.html
```
</details>

<details>
<summary><b>sitev2</b> - Django web app with service layer</summary>

```
sitev2/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── selectors.py
├── services.py
├── urls.py
├── views.py
├── migrations/
│   └── __init__.py
├── static/
│   └── app_name/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
├── templates/
│   └── app_name/
│       └── index.html
└── tests/
    ├── __init__.py
    ├── test_selectors.py
    ├── test_serices.py
    └── test_views.py
```
</details>

<details>
<summary><b>api</b> - Django REST Framework API</summary>

```
api/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── pagination.py
├── permissions.py
├── selectors.py
├── serializers.py
├── services.py
├── tests.py
├── urls.py
├── views.py
├── migrations/
│   └── __init__.py
└── tests/
    ├── __init__.py
    ├── test_api.py
    ├── test_selectors.py
    ├── test_serializers.py
    └── test_serices.py
```
</details>

<details>
<summary><b>api-graphql</b> - GraphQL API with Strawberry/Graphene</summary>

```
api-graphql/
├── __init__.py
├── admin.py
├── apps.py
├── inputs.py
├── middleware.py
├── models.py
├── mutations.py
├── queries.py
├── schema.py
├── services.py
├── types.py
├── urls.py
├── utils.py
├── migrations/
│   └── __init__.py
└── tests/
    ├── __init__.py
    ├── test_mutations.py
    ├── test_queries.py
    ├── test_shema.py
    └── test_types.py
```
</details>

<details>
<summary><b>websockets</b> - WebSocket-based application</summary>

```
websockets/
├── __init__.py
├── admin.py
├── apps.py
├── auth.py
├── consumers.py
├── events.py
├── exceptions.py
├── middleware.py
├── models.py
├── room.py
├── routing.py
├── selectors.py
├── services.py
├── tests.py
├── utils.py
├── views.py
├── migrations/
│   └── __init__.py
└── tests/
    ├── __init__.py
    ├── test_consumers.py
    ├── test_middleware.py
    └── test_routing.py
```
</details>

<details>
<summary><b>service-layer</b> - Service layer pattern</summary>

```
service-layer/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── selectors.py
├── services.py
├── urls.py
├── views.py
└── migrations/
    └── __init__.py
```
</details>

<details>
<summary><b>celery-tasks</b> - Celery async tasks</summary>

```
celery-tasks/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tasks.py
├── urls.py
├── views.py
└── migrations/
    └── __init__.py
```
</details>

<details>
<summary><b>admin-centric</b> - Django Admin focused</summary>

```
admin-centric/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
└── migrations/
    └── __init__.py
```
</details>

<details>
<summary><b>microservice</b> - Lightweight microservice</summary>

```
microservice/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── serializers.py
├── urls.py
├── views.py
└── migrations/
    └── __init__.py
```
</details>

<details>
<summary><b>ml-integration</b> - Machine Learning integration</summary>

```
ml-integration/
├── __init__.py
├── admin.py
├── apps.py
├── ml_utils.py
├── models.py
├── urls.py
├── views.py
└── migrations/
    └── __init__.py
```
</details>

Or create your own custom templates!

## Requirements

- Python >= 3.10
- Django >= 4.0

## Development

### Running Tests

```bash
pytest tests/
```

### Code Quality

This project uses:
- **Ruff** for linting and formatting
- **MyPy** for type checking
- **Pre-commit hooks** for automated checks

Setup pre-commit hooks:

```bash
pre-commit install
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Repository

GitHub: [https://github.com/DougVikt/dj-reframe](https://github.com/DougVikt/dj-reframe)

## Issues

If you encounter any issues or have suggestions, please file an issue on the [GitHub Issues](https://github.com/DougVikt/dj-reframe/issues) page.
