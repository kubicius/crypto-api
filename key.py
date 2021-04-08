from cryptography.fernet import Fernet


class Key():
    def generate(self):
        key = Fernet.generate_key()
        return key
