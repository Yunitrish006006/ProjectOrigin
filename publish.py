import paho.mqtt.client as mqtt
import random
import json
import datetime
import time
ISOTIMEFORMAT = '%m/%d %H:%M:%S'

client = mqtt.Client()

client.username_pw_set("yunitrish","0937565253")

client.connect("broker.emqx.io",1883,60)

while True:
    t0 = random.randint(0,30)
    btn1_clicked = random.randint(0,1)
    t = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    payload = {'button_1':btn1_clicked,'Time':t}

    print(json.dumps(payload))

    client.publish("yunitrish/Lamp",json.dumps(payload))
    time.sleep(2)