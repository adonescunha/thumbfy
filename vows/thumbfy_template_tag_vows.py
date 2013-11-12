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
from thumbfy.conf import THUMBFY_DEFAULT_SPEC


SPEC_ID = 'spec-id'
IMAGE_URL = 'http://localhost/some/image/url.jpg'


@Vows.batch
class ThumbfyTemplateTag(Vows.Context):

    class WhenSpecIdIsProvided(Vows.Context):

        def topic(self, topic):
            spec = Mock()
            spec_registry = Mock()
            spec_registry.get_spec_instance.return_value = spec
            thumbfy.templatetags.thumbfy.registry = spec_registry

            return (spec, spec_registry, thumbfy_tag(IMAGE_URL, SPEC_ID))

        def calls_generate_from_spec_registered_with_the_provided_id(self, topic):
            spec, spec_registry, _ = topic
            spec_registry.get_spec_instance.assert_called_with(SPEC_ID,
                    key=THUMBOR_SECURITY_KEY)
            spec.generate.assert_called_with(IMAGE_URL)

    class WhenSpecIdIsNotProvided(Vows.Context):

        def topic(self, topic):
            spec = Mock()
            spec_registry = Mock()
            thumbfy.templatetags.thumbfy.registry = spec_registry

            return (spec_registry, thumbfy_tag(IMAGE_URL))

        def fetch_default_spec_from_registry(self, topic):
            spec_registry, _ = topic
            spec_registry.get_spec_instance.assert_called_with(
                    THUMBFY_DEFAULT_SPEC, key=THUMBOR_SECURITY_KEY)
