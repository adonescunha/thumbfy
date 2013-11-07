from django.template import Library

from ..registry import registry


register = Library()

@register.simple_tag
def thumbfy(spec_id, image_url):
    spec = registry[spec_id]

    return spec.generate(image_url=image_url)
