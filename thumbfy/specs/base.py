from libthumbor import CryptoURL

class BaseThumbfySpec(object):

    def __init__(self, key=None):
        self.crypto = CryptoURL(key=key)

    def generate(self, **kwargs):
        return self.crypto.generate(**kwargs)
