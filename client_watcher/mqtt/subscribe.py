import threading
import time


class Subscribe(threading.Thread):
    def __init__(self, client_mqtt, topic: str, delay: int = 0):
        threading.Thread.__init__(self)
        self.client_mqtt = client_mqtt
        self.topic = topic
        self.delay = delay

    def receive_message(self, client, userdata, msg):  # noqa
        try:
            import json

            message = json.loads(msg.payload)
            print(f"received: {message}")

            if message.get("action") == "ping":
                self.client_mqtt.publish(
                    self.topic,
                    json.dumps({"action": "pong"}),
                )

        except Exception as e:
            print(f"Error in subscribe callback: {e}")
            print(f"Error in subscribe callback: {msg}")

    def subscribe(self):
        def on_message(client, userdata, msg):  # noqa
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        time.sleep(self.delay)

        self.client_mqtt.subscribe(self.topic)
        self.client_mqtt.on_message = self.receive_message

    def run(self):
        self.client_mqtt.loop_start()
        thread = threading.currentThread()
        self.subscribe()

        while getattr(thread, "do_run", True):
            time.sleep(0.1)
