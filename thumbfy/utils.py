from django.conf import settings
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule

def autodiscover():
    for app in settings.INSTALLED_APPS:
        mod = import_module(app)

        try:
            mod = import_module('%s.thumbfy_specs' % app)
        except:
            if module_has_submodule(mod, 'thumbfy_specs'):
                raise
