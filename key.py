from cryptography.fernet import Fernet
from validation import Validation
from storage import Storage


class Key:
    def generate(self):
        key = Fernet.generate_key()
        return key

    def setSymmetricKey(self, key):
        validation = Validation()
        if validation.validateHex(key):
            storage = Storage()
            if storage.writeKey('symmetric', key):
                return {"result": "Success!"}
            else:
                return {"result": "Key is valid but something went wrong."}
        else:
            return {"result": "Key is invalid."}

    def encodeSymmetric(self, string):
        storage = Storage()
        key = storage.readKey('symmetric')
        if key:
            f = Fernet(key)
            return {"result": True, "encoded": f.encrypt(string.encode())}
        else:
            return {"result": False}

    def decodeSymmetric(self, string):
        storage = Storage()
        key = storage.readKey('symmetric')
        if key:
            f = Fernet(key)
            return {"result": True, "encoded": f.decrypt(string.encode())}
        else:
            return {"result": False}