from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/symetric/key")
def get_symetric_key():
    """
    Returns random generated HEX key
    """
    return {"Hello": "World"}

@app.post("/symetric/key")
def set_symetric_key(key: str):
    """
    Sets passed HEX key on server
    """
    return {"key": key}

@app.post("/symetric/encode")
def encode_symetric(string: str):
    """
    Returns passed string but encoded
    """
    return {"string": string}

@app.post("/symetric/decode")
def decode_symetric(string: str):
    """
    Returns passed string but decoded
    """
    return {"string": string}

@app.get("/asymetric/key")
def get_asymetric_key():
    """
    Returns public and private HEX key and sets it on server
    """
    return {"key": "x"}

@app.get("/asymetric/key/ssh")
def get_asymetric_key_ssh():
    """
    Returns public and private HEX key in OpenSSH format
    """
    return {"key": "x"}

@app.get("/asymetric/key/ssh")
def get_asymetric_key_ssh(key: str):
    """
    Returns public and private HEX key in OpenSSH format
    """
    return {"key": "x"}

@app.post("/asymetric/key")
def set_asymetric_key(key: str):
    """
    Sets public and private HEX key on server
    """
    return {"key": "x"}

@app.post("/asymetric/sign")
def sign_asymetric(key: str):
    """
    Verifies current private key and returns signed string
    """
    return {"key": key}

@app.post("/asymetric/verify")
def verify_asymetric(key: str):
    """
    Using current public key verifies if string was signed
    """
    return {"key": key}

@app.post("/asymetric/encode")
def encode_asymetric(key: str):
    """
    Returns encoded string
    """
    return {"key": key}

@app.post("/asymetric/decode")
def decode_asymetric(key: str):
    """
    Returns decoded string
    """
    return {"key": key}