#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from thumbfy.registry import registry
from thumbfy.specs import BaseThumbfySpec


registry.register('testapp1:spec', BaseThumbfySpec)
