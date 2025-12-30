#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import keyboard
import threading

MQTT_BROKER = "localhost"
MQTT_PORT   = 1883
MQTT_TOPIC  = "homeassistant/barcode_scanner"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

buffer = ""

def on_key(event):
    global buffer
    if len(event.name) == 1:
        buffer += event.name
    elif event.name in ("enter", "return"):
        client.publish(MQTT_TOPIC, payload=buffer, qos=0, retain=False)
        print(f"Sent: {buffer}")
        buffer = ""

keyboard.on_release(on_key)
threading.Event().wait()
