#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from django.template import Library
from django_thumbor.conf import THUMBOR_SECURITY_KEY, THUMBOR_SERVER

from ..registry import registry
from ..conf import THUMBFY_DEFAULT_SPEC


register = Library()


@register.simple_tag
def thumbfy(obj, spec_id=None):
    if not spec_id:
        spec_id = THUMBFY_DEFAULT_SPEC

    spec = registry.get_spec_instance(spec_id, key=THUMBOR_SECURITY_KEY)

    return '%s%s' % (THUMBOR_SERVER, spec.generate(obj))
