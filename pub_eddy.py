# MAX first recieve inputs through NI-MAX 
import numpy as np
import random
import time
import datetime

from paho.mqtt import client as mqtt_client

import nidaqmx
task = nidaqmx.Task()
task.ai_channels.ai_current_acrms_units("AC01/ai0")

task.start()

eddy = task.read()
#broker = 'tc18c09c-internet-facing-87a92e25fe73b3be.elb.ap-south-1.amazonaws.com'
broker = 'localhost'
port = 1884
topic = "sensor/eddy_current"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
	
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username="shaury", password="test")
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    time_then = time.time()
    f = 0
    while True:
        msg = str(eddy)
        result = client.publish(topic, msg,qos=1)
        status = result[0]
        		if status == 0:
        			print(f"Send `{msg}` to topic `{topic}`")
        		else:
        			print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
    
task.stop()
task.close()