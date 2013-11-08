from django.template import Library
from django_thumbor.conf import THUMBOR_SECURITY_KEY

from ..registry import registry


register = Library()

@register.simple_tag
def thumbfy(spec_id, image_url):
    spec = registry.get_spec_instance(spec_id, key=THUMBOR_SECURITY_KEY)

    return spec.generate(image_url=image_url)
