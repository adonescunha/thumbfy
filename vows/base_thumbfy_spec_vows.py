#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect
from mock import Mock
from libthumbor import CryptoURL
from thumbfy.specs import BaseThumbfySpec


KEY = 'SAMPLE-KEY'
IMAGE_URL = '/image/url.jpg'


@Vows.batch
class BaseThumbfySpecVows(Vows.Context):

    def topic(self):
        return BaseThumbfySpec(key=KEY)

    class Crypto(Vows.Context):

        def topic(self, spec):
            return spec.crypto

        def is_a_cryptourl_instance(self , crypto):
            expect(crypto).to_be_instance_of(CryptoURL)

        def has_the_same_key_as_spec_has(self, crypto):
            expect(crypto.key).to_equal(KEY)

    class Generate(Vows.Context):

        def topic(self):
            spec = BaseThumbfySpec(key=KEY)
            spec.crypto = Mock(spec=CryptoURL)
            spec.generate(image_url=IMAGE_URL)
            return (spec, IMAGE_URL)

        def calls_crypto_generate_with_passed_kwargs(self, topic):
            spec, image_url = topic
            spec.crypto.generate.assert_called_with(image_url=image_url)

    class GetUrlSchema(Vows.Context):

        def topic(self):
            spec = BaseThumbfySpec(key=KEY)
            test_cases = (
                {},
                {'width': 100, 'height': 100}
            )

            for url_schema in test_cases:
                spec.url_schema = url_schema
                yield (spec.get_url_schema(IMAGE_URL), IMAGE_URL, url_schema)

        def returns_a_dict_containing_the_image_url_plus_provided_schema(
                self, topic):
            result, image_url, schema = topic
            expected = {'image_url': image_url}
            expected.update(schema)
            expect(result).to_equal(expected)
