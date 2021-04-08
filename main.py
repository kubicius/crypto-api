from fastapi import FastAPI
from key import Key


app = FastAPI()
keyObj = Key()

@app.get("/symmetric/key")
def get_symmetric_key():
    """
    Returns random generated HEX key
    """
    return keyObj.generate().hex()

@app.post("/symmetric/key")
def set_symmetric_key(key: str):
    """
    Sets passed HEX key on server
    """
    return keyObj.setSymmetricKey(key)

@app.post("/symmetric/encode")
def encode_symmetric(string: str):
    """
    Returns passed string but encoded
    """
    return keyObj.encodeSymmetric(string)

@app.post("/symmetric/decode")
def decode_symmetric(string: str):
    """
    Returns passed string but decoded
    """
    return keyObj.decodeSymmetric(string)

@app.get("/asymmetric/key")
def get_asymmetric_key():
    """
    Returns public and private HEX key and sets it on server
    """
    return {"key": "x"}

@app.get("/asymmetric/key/ssh")
def get_asymmetric_key_ssh():
    """
    Returns public and private HEX key in OpenSSH format
    """
    return {"key": "x"}

@app.get("/asymmetric/key/ssh")
def get_asymmetric_key_ssh(key: str):
    """
    Returns public and private HEX key in OpenSSH format
    """
    return {"key": "x"}

@app.post("/asymmetric/key")
def set_asymmetric_key(key: str):
    """
    Sets public and private HEX key on server
    """
    return {"key": "x"}

@app.post("/asymmetric/sign")
def sign_asymmetric(key: str):
    """
    Verifies current private key and returns signed string
    """
    return {"key": key}

@app.post("/asymmetric/verify")
def verify_asymmetric(key: str):
    """
    Using current public key verifies if string was signed
    """
    return {"key": key}

@app.post("/asymmetric/encode")
def encode_asymmetric(key: str):
    """
    Returns encoded string
    """
    return {"key": key}

@app.post("/asymmetric/decode")
def decode_asymmetric(key: str):
    """
    Returns decoded string
    """
    return {"key": key}