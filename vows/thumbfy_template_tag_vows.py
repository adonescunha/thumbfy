from pyvows import Vows, expect
from mock import Mock

import thumbfy
from thumbfy.registry import SpecRegistry
from thumbfy.templatetags.thumbfy import thumbfy as thumbfy_tag


SPEC_ID = 'spec-id'
IMAGE_URL = 'http://localhost/some/image/url.jpg'

@Vows.batch
class ThumbfyTemplateTag(Vows.Context):

    def topic(self):
        spec = Mock()
        spec_registry = SpecRegistry()
        spec_registry.register(SPEC_ID, spec)
        thumbfy.templatetags.thumbfy.registry = spec_registry

        return (spec, thumbfy_tag(SPEC_ID, IMAGE_URL))

    def call_generate_from_spec_registered_with_the_provided_id(self, topic):
        spec = topic[0]
        spec.generate.assert_called_with(image_url=IMAGE_URL)
