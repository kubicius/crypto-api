class Storage:
    def writeKey(self, type, key):
        file = open('keys/'+type+'.key', 'wb')
        if file.write(key.encode()):
            return True
        else:
            return False

    def readKey(self, type):
        return bytes.fromhex(open('keys/' + type + '.key', 'r').read())

