#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from django.conf import settings

THUMBFY_DEFAULT_SPEC = getattr(settings, 'THUMBFY_DEFAULT_SPEC', None)
