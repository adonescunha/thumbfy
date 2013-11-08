#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from libthumbor import CryptoURL


class BaseThumbfySpec(object):

    def __init__(self, key=None):
        self.crypto = CryptoURL(key=key)

    def generate(self, **kwargs):
        return self.crypto.generate(**kwargs)
