from pyvows import Vows, expect

from thumbfy.registry import registry
from thumbfy.utils import autodiscover


@Vows.batch
class AutoDiscoverVows(Vows.Context):

    def topic(self):
        autodiscover()
        test_cases = (
            'testapp1:spec',
            'testapp2:spec1',
            'testapp2:spec2'
        )

        for test_case in test_cases:
            yield (test_case, registry)

    def installed_apps_specs_are_registered(self, topic):
        test_case, registry = topic
        expect(registry.specs.has_key(test_case)).to_be_true()
