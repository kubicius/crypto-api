

class Storage:
    """
    Class destined to make storage operations.
    """

    def writeKey(self, type, key):
        file = open('keys/'+type+'.key', 'w')
        if file.write(key):
            return True
        else:
            return False

    def readKey(self, type):
        return bytes.fromhex(open('keys/' + type + '.key', 'r').read())

