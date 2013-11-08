from .exceptions import AlreadyRegistered, NotRegistered


def _raise_not_registered_error(id):
    raise NotRegistered('The id %s is not registered' % id)

class SpecRegistry(object):

    def __init__(self):
        self.specs = {}

    def __getitem__(self, key):
        try:
            return self.specs[key]
        except KeyError:
            _raise_not_registered_error(key)

    def register(self, id, spec):
        if self.specs.has_key(id):
            raise AlreadyRegistered('The spec with id %s is already '
                'registered' % id)

        self.specs[id] = spec

    def unregister(self, id):
        try:
            del self.specs[id]
        except KeyError:
            _raise_not_registered_error(id)

    def get_spec_instance(self, spec_id, **kwargs):
        return self.specs[spec_id](**kwargs)

registry = SpecRegistry()
