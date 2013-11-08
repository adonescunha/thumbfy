#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from libthumbor import CryptoURL


class BaseThumbfySpec(object):

    default_thumb_url = ''
    url_schema = {}

    def __init__(self, key=None):
        self.crypto = CryptoURL(key=key)

    def get_url_schema(self, image_url):
        schema = {'image_url': image_url}
        schema.update(self.url_schema)

        return schema

    def generate(self, obj):
        if isinstance(obj, basestring):
            image_url = obj
        else:
            try:
                image_url = obj.url
            except ValueError:
                image_url = self.default_thumb_url

        return self.crypto.generate(**self.get_url_schema(image_url))
