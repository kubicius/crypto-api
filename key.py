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
            if storage.writeKey(type, key):
                return {"result": "Success!"}
            else:
                return {"result": "Key is valid but something went wrong."}
        else:
            return {"result": "Key is invalid."}

    def setRandomAssymetricKeys(self):
        storage = Storage()
        private = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        pem = private.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()
        public = private.public_key()
        publicPem = public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).hex()
        print(private.RSAPrivateKey)
        if storage.writeKey('public', publicPem) and storage.writeKey('private', pem):
            return {"result": True, "public": public, "private": private}
        else:
            return {"result": "Error occured."}

    def generateRandomOpenSshKeys(self):
        private = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        pem = private.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()
        public = private.public_key()
        publicPem = public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).hex()

        return {"public": publicPem, "private": pem}