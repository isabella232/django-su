from django.conf import settings


def import_function(name, package=None):
    path = name.split('.')
    module_path = '.'.join(path[:-1])
    try:
        from django.utils.importlib import import_module
        module = import_module(module_path, package)
    except ImportError:  # compatible with old version of Django
        module = __import__(module_path, {}, {}, path[-1])
    return getattr(module, path[-1])


def can_su_login(user):
    su_login = getattr(settings, 'SU_LOGIN', None)
    if su_login:
        return import_function(su_login)(user)
    return user.has_perm('auth.change_user')
