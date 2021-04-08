from fastapi import FastAPI
from key import Key
from cipher import Cipher


app = FastAPI()
keyObj = Key()
cipherObj = Cipher()

@app.get("/symmetric/key")
def get_symmetric_key():
    """
    Returns random generated HEX key
    """
    return keyObj.generate()

@app.post("/symmetric/key")
def set_symmetric_key(key: str):
    """
    Sets passed HEX key on server
    """
    return keyObj.setKey('symmetric', key)

@app.post("/symmetric/encode")
def encode_symmetric(string: str):
    """
    Returns passed string but encoded
    """
    return cipherObj.encodeSymmetric(string)

@app.post("/symmetric/decode")
def decode_symmetric(string: str):
    """
    Returns passed string but decoded
    """
    return cipherObj.decodeSymmetric(string)

@app.get("/asymmetric/key")
def get_asymmetric_key():
    """
    Returns public and private random HEX key and sets it on server
    """
    return keyObj.setRandomAssymetricKeys()

@app.get("/asymmetric/key/ssh")
def get_asymmetric_key_ssh():
    """
    Returns public and private HEX key in OpenSSH format
    """
    return keyObj.generateRandomOpenSshKeys()

@app.post("/asymmetric/key")
def set_asymmetric_key(public: str, private: str):
    """
    Sets public and private HEX key on server
    """
    if keyObj.setKey('public', public) and keyObj.setKey('private', private):
        return {"result": "Success!"}
    else:
        return {"result": "Keys are invalid."}

@app.post("/asymmetric/sign")
def sign_asymmetric(string: str):
    """
    Using current public key signs and returns string
    """
    return cipherObj.sign(string)

@app.post("/asymmetric/verify")
def verify_asymmetric(string: str):
    """
    Using current public key verifies if string was signed
    """
    return cipherObj.verify(string)

@app.post("/asymmetric/encode")
def encode_asymmetric(string: str):
    """
    Returns encoded string
    """
    return cipherObj.encodeAsymmetric(string)

@app.post("/asymmetric/decode")
def decode_asymmetric(string: str):
    """
    Returns decoded string
    """
    return cipherObj.decodeAsymmetric(string)