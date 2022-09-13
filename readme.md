## Pub_eddy.py - 
Contains the code for publishing the temperature sensors values using NI-DAQ and MQTT protocol .
This code uses NI-DAQ AC01 port used for current sensors. 
The commented lines have broker where we can define the name of external broker as well, in this case we are using local host Mosquitto broker.
A mosquitto broker must be installed on the local machine or we can use online mqtt broker as well.
 
## Pub.py - 
Contains the code for publishing the eddy current sensors values using NI-DAQ and MQTT protocol .
This code uses NI-DAQ thrmcpl TC01 port used for temperature sensors. 
The commented lines have broker where we can define the name of external broker as well, in this case we are using local host Mosquitto broker.

## Sub1.py - 
Contains the code for subscribing(receiving) the temperature sensors values and eddy current values using  MQTT protocol. 
In this code the doQuery function is pushing the values into the database defined by sql.py. 
We are using the pos =1 , pos = 0 for two simlultaneous connections. 

## Sql.py -  
Contains the code for the schema of the database used for storing the sensors values . 
This code has the columns and the basic data types required for that. The data-time column is the primary key and hence cannot be NULL and cannot be repeated. 

## How to send messages for local host-
open terminal and run 
###  moquitto -p 1884 //wait for it to establish connection
### python3 pub.py
### python3 pub_eddy.py

## How to recieve messages 
open terminal 
### python3 sub1.py

## sql.py - 
This script is only to be run once as the schema is made only once hence once the table is made this script is not required.
open terminal 
### python3 sql.py //given you have access to mysql on local host
 
