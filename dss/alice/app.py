import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
from flask import Flask, request, redirect, session, jsonify
import time
import json
from helpers import *
from key_exchange import *
from users import *
from elgamal_dss import *
import json

app = Flask(__name__)
app.debug = True
app.secret_key = "a secret key"

keys = {"bob_pub":None}
message_received = {"m":None}

@app.route("/mypk")
def my_pk():
    """Frontend sends request to display the Alice's public key stored in backend."""
    if request.method == 'GET':
        alice_pk = ALICE.public_key()
        return str(alice_pk)
    return ""

@app.route("/publicKey")
def bob_key():
    """Frontend sends the public key of Bob along a GET request to be stored in backend and compute DSS."""
    if request.method == 'GET':
        bobKey =request.args.get('bobKey')
        keys["bob_pub"] = bobKey
        return "Bob's public key is registred!"
    return ""

@app.route("/getpub" , methods=["POST"])
def send_pub():
    """ Responds with the its public key and sends the public key of sender to front end."""
    print(ALICE)
    if request.method == 'POST':
        # post responses with the plain text in many other layers.
        req_value = (request.values).to_dict()
        # extract the key from alice respones in post req.  
        bob_pk =  list(req_value.keys())[0] 
        if keys["bob_pub"] != str(bob_pk):
            keys["bob_pub"] = str(bob_pk)
        return str(ALICE.public_key())
    return ""

@app.route("/getmsg")
def getmsg():
    """ Signs a message and send it the other user."""
    if request.method == 'GET':
        # read the secret file and remove spaces to encrypt and tranmsitt
        msg = read_remove_spaces("..\messages\msgAlice.txt")
        #sign the message before the encryption
        signature = sign_message(ALICE.g, ALICE.q, ALICE.private_key, msg)
        signed_msg = {"msg": msg,"signature": signature}
        return json.dumps(signed_msg)
    return ""

@app.route("/msg", methods=["POST"])
def msg():
    """Gets a message sends from other user and verify its signature."""
    if request.method == 'POST':     
        data = request.json
        message = data["message"]
        signature = data["sign"]
        valid = verify_signature(ALICE.g, ALICE.q, int(keys["bob_pub"]), message, signature)
        if valid:
            message_received["m"] = message
            return "Message is validated!"
        else:
            message_received["m"] ="The Digtial Signature is not valid!"
            return "The Digtial Signature is not valid."
    return ""

@app.route("/dispaly_msg", methods=["GET"])
def dispaly_msg():
    """Every 5 second check if there is a message to be displayed in front end."""
    try:
        if message_received["m"] != None:
            return str(message_received["m"])
        else:
            return ""
    except Exception as e:
        print(e.__str__())


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response 

@app.route("/")
def index():
    return app.send_static_file("alice.html")

if __name__ == "__main__":
    app.run()
