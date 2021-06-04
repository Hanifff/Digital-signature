
/**
 * Funtion publicKeyExchange(), gets the Bob's public key in the backend to be sent to Alice.
 */
function publicKeyExchange(){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            getPk(result)
        }
    };
    xhr.open("GET", "http://127.0.0.1:5500/mypk", true);
    xhr.send(null);
}

/**
 * Function getPk() sends request to Alice to get her Public key.
 * The responded public key will be displayed in the Bob's front-end.
 */
function getPk(mypk){
    document.getElementById("pk_div").style.display = 'none'
    document.getElementById("display_pk").style.display = 'block'
    document.getElementById("cipher_div").style.display = "block"
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
    try{
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            document.getElementById("dis_pk").innerHTML = '<strong> '+result +'</strong>' // show Alice's public key in Bob webpage 
            alicesKey(result)  
        }
    }catch(err) {
        return err;
        }   
    };
    xhr.open("POST","http://127.0.0.1:5000/getpub", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(mypk);
}

/**
 * Function alicesKey() sends the public key of Alice simulantlously to the Bob's back-end.
 * @param {} key Alice's public key 
 */
function alicesKey(key){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            console.log(result)
        }
    };
    xhr.open("GET", "http://127.0.0.1:5500/publicKey?aliceKey="+key, true);
    xhr.send(null);
}

/**
 * Function getMsg() sents request to Bob to get her message in encryptet mode. 
 * The response is sent to Bob to be decryptet.
 */
function getMsg() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            var parsResult = JSON.parse(result)
            var msgToAlice = JSON.stringify({message: parsResult.msg, sign: parsResult.signature})
            sendToAlice(msgToAlice)
            document.getElementById("cipher_div").style.display = 'none'
        }
    };
    xhr.open("GET", "http://127.0.0.1:5500/getmsg", true);
    xhr.send(null);
}

/***
 * Function sendToBob(msg) sends post request with the encryptet message of Alice to Bob.
 * Bob decrypt the message using the secret key created by public key of Alice.
 * The result will be displayed in Bob's front-end. 
 * @param {} msg Encryptet message from Alice
 */
function sendToAlice(msg) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById("sent").innerHTML = "Your message is signed and sent!"
        }
    };
    xhr.open("POST", "http://127.0.0.1:5000/msg", true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.send(msg);
}
/**
* Function dispalyMsg, displayes the decrypted message which has a valid digital signature.
*/
function dispalyMsg(){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            if (result != ""){
                document.getElementById("comment").innerHTML = "This message has a valid Digital Signature:" 
                document.getElementById("msg").innerHTML = result;
            }
            else{
                console.log("No message")
            }
        }
    };
    xhr.open("GET", "http://127.0.0.1:5500/dispaly_msg", true);
    xhr.send(null);
}
// check if there is a message to show every 5 sec
setInterval(dispalyMsg,5*1000)
