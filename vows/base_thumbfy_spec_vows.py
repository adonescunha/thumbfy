from pyvows import Vows, expect
from mock import Mock
from libthumbor import CryptoURL
from thumbfy.specs import BaseThumbfySpec


KEY = 'SAMPLE-KEY'

@Vows.batch
class BaseThumbfySpecVows(Vows.Context):

    def topic(self):
        return BaseThumbfySpec(key=KEY)

    class Crypto(Vows.Context):

        def topic(self, spec):
            return spec.crypto

        def should_be_a_cryptourl_instance(self , crypto):
            expect(crypto).to_be_instance_of(CryptoURL)

        def should_have_the_same_key_as_spec_has(self, crypto):
            expect(crypto.key).to_equal(KEY)

    class Generate(Vows.Context):

        def topic(self):
            return {'width': 50, 'height': 50}

        def should_call_crypto_generate_with_passed_kwargs(self, kwargs):
            spec = BaseThumbfySpec(key=KEY)
            spec.crypto = Mock(spec=CryptoURL)
            spec.generate(**kwargs)
            spec.crypto.generate.assert_called_with(**kwargs)
