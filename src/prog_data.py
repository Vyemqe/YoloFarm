import random       # For sample data
import time
import  sys
from  Adafruit_IO import  MQTTClient

AIO_FEED_ID = ""    # Name of the feed to be subscribed
AIO_USERNAME = ""   # Adafruit IO username
AIO_KEY = ""        # Hash key for the Adafruit IO account

###! MQTT implementation - BEGIN ###
def connected(client):
    print("[CONNECTED] Successfully connected to Adafruit IO!")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("[SUBSCRIBE] Successfully subscribed to feed ID: " + AIO_FEED_ID)
    """
    Do something
    """

def disconnected(client):
    print("[DISCONNECTED] Disconnected from Adafruit IO!")
    sys.exit(1)

def message(client , feed_id , payload):
    print("[MESSAGE] Received message on feed ID: " + feed_id + " with payload: " + payload)
    """
    Do something
    """
###! MQTT implementation - END ###

# Python Gateway configuration
client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    value = random.randint(0, 100)      # Sampling data, replace with actual sensor readings

    print("[UPDATE] Updating value: ", value)
    client.publish("bbc-temp", value)   # Assume the sample Feed is 'bbc-temp'

    time.sleep(30)          # Update every 30 seconds