from pyvows import Vows, expect
from mock import Mock

from thumbfy.registry import SpecRegistry
from thumbfy.exceptions import AlreadyRegistered, NotRegistered


SPEC_ID = 'spec-id'

@Vows.batch
class SpecRegistryVows(Vows.Context):

    def topic(self):
        return SpecRegistry()

    def is_initialized_with_an_empty_specs_dict(self, registry):
        expect(registry.specs).to_equal({})

    class RegisterVows(Vows.Context):

        def topic(self, registry):
            spec = Mock()
            registry.register(SPEC_ID, spec)
            return (registry, spec)

        def add_the_id_provided_to_specs_dict_as_key(self, topic):
            registry = topic[0]
            expect(registry.specs.has_key(SPEC_ID)).to_be_true()

        def add_the_spec_provided_to_specs_dict_as_value(self, topic):
            registry, spec = topic
            expect(registry.specs[SPEC_ID]).to_equal(spec)

        class WhenIdWasAlreadyRegistered(Vows.Context):

            def topic(self, topic):
                registry, spec = topic
                return registry.register(SPEC_ID, Mock('another-spec'))

            def raises_already_registered_error(self, topic):
                expect(topic).to_be_an_error_like(AlreadyRegistered)

    class UnregisterVows(Vows.Context):

        def topic(self):
            return SpecRegistry()

        class WhenIdIsNotRegistered(Vows.Context):

            def topic(self, registry):
                return registry.unregister(SPEC_ID)

            def raises_not_registered_error(self, topic):
                expect(topic).to_be_an_error_like(NotRegistered)

        class WhenIdIsRegistered(Vows.Context):

            def topic(self, registry):
                registry.specs = {SPEC_ID: Mock()}
                registry.unregister(SPEC_ID)
                return registry

            def removes_id_from_specs_dict(self, registry):
                expect(registry.specs.has_key(SPEC_ID)).to_be_false()
