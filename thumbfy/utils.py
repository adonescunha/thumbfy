#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


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
