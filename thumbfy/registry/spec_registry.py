from ..exceptions import AlreadyRegistered, NotRegistered

class SpecRegistry(object):

    def __init__(self):
        self.specs = {}

    def register(self, id, spec):
        if self.specs.has_key(id):
            raise AlreadyRegistered('The spec with id %s is already '
                'registered' % id)

        self.specs[id] = spec

    def unregister(self, id):
        try:
            del self.specs[id]
        except KeyError:
            raise NotRegistered('The id %s is not registered' % id)
