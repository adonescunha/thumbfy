#!/usr/bin/env python
# -*- coding: utf-8 -*-

# thumbfy
# https://github.com/adonescunha/thumbfy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


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
            spec_class = Mock
            registry.register(SPEC_ID, spec_class)
            return (registry, spec_class)

        def add_the_id_provided_to_specs_dict_as_key(self, topic):
            registry = topic[0]
            expect(registry.specs.has_key(SPEC_ID)).to_be_true()

        def add_the_spec_provided_to_specs_dict_as_value(self, topic):
            registry, spec_class = topic
            expect(registry.specs[SPEC_ID]).to_equal(spec_class)

        class WhenIdWasAlreadyRegistered(Vows.Context):

            def topic(self, topic):
                registry, spec_class = topic
                return registry.register(SPEC_ID, Mock)

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
                registry.specs = {SPEC_ID: Mock}
                registry.unregister(SPEC_ID)
                return registry

            def removes_id_from_specs_dict(self, registry):
                expect(registry.specs.has_key(SPEC_ID)).to_be_false()

    class GetVows(Vows.Context):

        class WhenSpecIsRegistered(Vows.Context):

            def topic(self):
                registry = SpecRegistry()
                spec = Mock
                registry.specs = {SPEC_ID: spec}
                return (spec, registry[SPEC_ID])

            def returns_spec_registered_using_id_provided(self, topic):
                expected, actual = topic
                return expect(expected).to_equal(actual)

        class WhenSpecIsNotRegistered(Vows.Context):

            def topic(self):
                registry = SpecRegistry()
                return registry[SPEC_ID]

            def raises_not_registered_error(self, topic):
                expect(topic).to_be_an_error_like(NotRegistered)

    class GetSpecInstance(Vows.Context):

        def topic(self):
            registry = SpecRegistry()
            spec_class = Mock
            registry.specs = {SPEC_ID: spec_class}
            return (spec_class, registry.get_spec_instance(SPEC_ID,
                key='THUMBOR-KEY'))

        def returns_an_instance_of_the_spec_registered(self, topic):
            spec_class, spec = topic
            expect(spec).to_be_instance_of(spec_class)
