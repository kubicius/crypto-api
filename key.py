from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from validation import Validation
from storage import Storage


class Key:
    """
    Class meant to generate and modify keys.
    """
    def generate(self):
        key = Fernet.generate_key().hex()
        return key

    def setKey(self, type, key):
        validation = Validation()
        valid = False
        if type == 'symmetric':
            if validation.validateSymmetricHex(key):
                valid = True
        else:
            if validation.validateAsymmetricHex(key):
                valid = True
        if valid:
            storage = Storage()
            if storage.writeKey(type, key.encode()):
                return {"result": "Success!"}
            else:
                return {"result": "Key is valid but something went wrong."}
        else:
            return {"result": "Key is invalid."}

    def generatePrivateKey(self):
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

    def preparePrivatePem(self, private, format):
        return private.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=format,
            encryption_algorithm=serialization.NoEncryption()
        )

    def preparePublicPem(self, public):
        return public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def setRandomAssymetricKeys(self):
        storage = Storage()
        private = self.generatePrivateKey()
        pem = self.preparePrivatePem(private, format=serialization.PrivateFormat.TraditionalOpenSSL)
        public = private.public_key()
        publicPem = self.preparePublicPem(public)

        if storage.writeKey('public', publicPem) and storage.writeKey('private', pem):
            return {"result": True, "public": publicPem.hex(), "private": pem.hex()}
        else:
            return {"result": "Error occured."}

    def generateRandomOpenSshKeys(self):
        private = self.generatePrivateKey()
        pem = self.preparePrivatePem(private, format=serialization.PrivateFormat.OpenSSH)
        public = private.public_key()
        publicPem = self.preparePublicPem(public)

        return {"public": publicPem.hex(), "private": pem.hex()}