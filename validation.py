class Validation:
    def validateHex(self, key):
        try:
            int(key, 16)
            return True
        except ValueError:
            return False