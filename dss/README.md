# DAT510 Asssignment 1, 2020 
This file contains information both about which packages need to be installed and the structure of the project.<br>
-------------------------------------------------------------------------------------

## Requirements packages 
In order to run the scripts, the last python version (3.7.x) is required.<br>

Flask need to be installed<br>
https://flask.palletsprojects.com/en/1.1.x/installation/<br>

--------------------------------------------------------------------------------------

## File structures and Running the code
The elgamal_dss.py contains the implementation of the Elgamal Digital Siganature Scheme algorithm.
The key_exchange.py contains a class for the key exchange algorithm.<br>
The global_paramteres.py contains implementation of the cyclic group and primitive roots.<br>
The helper.py contians helper functions for the porject.<br>
The users.py contains two dh objects, Alice and Bob.<br>
Alice's web server and front-end is in the folder alice.<br>
Bob's web server and front-end is in the folder bob.<br>
The directory alice/staticcontains the HTML and javascript file for the front-end<br>
The directory bob/staticcontains the HTML and javascript file for the front-end<br>
The messages folder contains files with plaintext for both Alice and Bob.<br>

--------------------------------------------------------------------------------------

## Command to run the apps
Run the webserver Alice:<br>
cd alice<br>
app.py<br>
Run the webserver Bob:<br>
cd bob<br>
app.py<br>

---------------------------------------------------------------------------------------

Log will be shown after first time Alice or Bob sends request.<br>