from __future__ import print_function
import datetime
import time
import random
from paho.mqtt import client as mqtt_client
import mysql.connector
import paho.mqtt.client as mqtt
import ssl


hostname = 'localhost'
username = 'root'
password = '********'
database = 'sensors'


def doQuery( conn, time_stamp,T0,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,e1,e2,e3,e4,e5 ) :
    cur = conn.cursor()
    cur.execute('INSERT INTO sensors VALUES'+str((time_stamp,T0,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,e1,e2,e3,e4,e5))+';');
    conn.commit()
	
print( "Using mysql.connector:" )
import mysql.connector
myConnection = mysql.connector.connect(host=hostname,passwd=password,user=username,db=database,auth_plugin='mysql_native_password')



#broker = 'tc18c09c-internet-facing-87a92e25fe73b3be.elb.ap-south-1.amazonaws.com'
broker = 'localhost'
port = 1884
topic = [("sensor/temprature",2),("sensor/eddy_current",1)]
client_id = f'python-mqtt-{random.randint(0, 100)}'
prev_temprature,F,e1,e2,e3,e4,e5= 0,0,0,0,0,0,0

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.username_pw_set(username="shaury", password="test")
    print("Connecting...")
    client.connect(broker, port)
    return client
    
def subscribe(client: mqtt_client):
	def on_message(client, userdata, msg):
		global e1,e2,e3,e4,e5,prev_temprature,F;
		MSG = msg.payload.decode();f = [float(i) for i in MSG.replace('[','').replace(']','').split(',')];
		if(msg.topic=='sensor/eddy_current'):		
			if(f[0]==100 and e1!=0):
				try:
					doQuery( myConnection,datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),prev_temprature[0],prev_temprature[1],prev_temprature[2],prev_temprature[3],prev_temprature[4],prev_temprature[5],prev_temprature[6],prev_temprature[7],prev_temprature[8],prev_temprature[9],prev_temprature[10],prev_temprature[11],prev_temprature[12],prev_temprature[13],round(e1,3),round(e2,3),round(e3,3),round(e4,3),round(e5,3));
					print((datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),prev_temprature[0],prev_temprature[1],prev_temprature[2],prev_temprature[3],prev_temprature[4],prev_temprature[5],prev_temprature[6],prev_temprature[7],prev_temprature[8],prev_temprature[9],prev_temprature[10],prev_temprature[11],prev_temprature[12],prev_temprature[13],e1,e2,e3,e4,e5));
				except:
					pass#print(E);
				e1 = e2 = e3 = e4 = e5 = 0;
			elif(f[0]!=100):
				e1 = max(f[0],e1);e2 = max(f[1],e2);e3 = max(f[2],e3);e4 = max(f[3],e4);e5 = max(f[4],e5);
		else:
			prev_temprature = f;			
	client.subscribe(topic)
	client.on_message = on_message
    	
    	
    
def run():
    client = connect_mqtt()
    print(subscribe(client))
    client.loop_forever()
if __name__ == '__main__':
    run()

myConnection.close()
