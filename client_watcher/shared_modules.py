import threading

from client_watcher.mqtt.connect import Connector

client_mqtt = Connector().client_mqtt
lock = threading.Lock()
