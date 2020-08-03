"""Constants used by the deployment script"""
from askbot.utils.console import bold

DEFAULT_PROJECT_NAME = 'askbot_site'
DEFAULT_MEDIA_ROOT_SUBDIR = 'upfiles'
DEFAULT_STATIC_ROOT_SUBDIR = 'static'

SQLITE = 2
DATABASE_ENGINE_CHOICES = (
    (1, 'PostgreSQL'),
    (SQLITE, 'SQLite'),
    (3, 'MySQL'),
    (4, 'Oracle')
)

ROOT_DIR_HELP = 'the ' + bold('Root') + \
        ' directory path (relative or absolute).\n' + \
        'This directory will contain the Django project\'s manage.py file'

PROJ_NAME_HELP = 'the ' + bold('Project') + \
        ' directory name.\nWill be a subdirectory within the ' + \
        bold('Root') + ' for the settings.py, urls.py files'

MEDIA_ROOT_HELP = 'value of the ' + bold('MEDIA_ROOT') + \
        ' setting for the settings.py file.\n ' + \
        'This directory is for the user uploaded files.\n ' + \
        'Default is /upfiles within the ' + bold('Root') + ' directory.'

DOMAIN_NAME_HELP = 'domain name of your Askbot site. Used for the ' + \
        bold('ALLOWED_DOMAINS') + ' setting.'

LANGUAGE_CODE_HELP = 'two or four letter with a dash language code (e.g. ' + \
        bold('fr') + ', ' + bold('de') + ', ' + bold('zh_CN') + '.\n ' + \
        'Value of the ' + bold('LANGUAGE_CODE') + ' setting.\n ' + \
        'Default value is ' + bold('en') + '.'

DATABASE_ENGINE_HELP = 'database engine, type 1 for PostgreSQL, 2 for SQLite, ' + \
        '3 for MySQL, 4 for Oracle.'

USE_FORCE_PARAMETER = 're-run askbot-setup with a --force parameter'
