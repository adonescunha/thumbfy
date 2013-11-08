#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect
from mock import Mock
from django_thumbor.conf import THUMBOR_SECURITY_KEY, THUMBOR_SERVER

import thumbfy
from thumbfy.registry import SpecRegistry
from thumbfy.specs import BaseThumbfySpec
from thumbfy.templatetags.thumbfy import thumbfy as thumbfy_tag


SPEC_ID = 'spec-id'
IMAGE_URL = 'http://localhost/some/image/url.jpg'


@Vows.batch
class ThumbfyTemplateTag(Vows.Context):

    def topic(self):
        spec = Mock()
        spec_registry = Mock()
        spec_registry.get_spec_instance.return_value = spec
        thumbfy.templatetags.thumbfy.registry = spec_registry

        return (spec, spec_registry, thumbfy_tag(SPEC_ID, IMAGE_URL))

    def call_generate_from_spec_registered_with_the_provided_id(self, topic):
        spec, spec_registry, _ = topic
        spec_registry.get_spec_instance.assert_called_with(SPEC_ID,
                key=THUMBOR_SECURITY_KEY)
        spec.generate.assert_called_with(image_url=IMAGE_URL)
