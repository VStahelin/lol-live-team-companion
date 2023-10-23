import threading
import time

from constants import MqttMessage


class Subscriber(threading.Thread):
    def __init__(self, client_mqtt, delay: int = 0):
        self.thread = threading.Thread.__init__(self)
        self.client_mqtt = client_mqtt
        self.delay = delay

    def receive_message(self, client, userdata, msg):  # noqa
        try:
            import json

            message = json.loads(msg.payload)
            self.message_handler(message)

        except Exception as e:
            print(f"Error in subscribe callback: {e}")
            print(f"Error in subscribe callback: {msg}")

    def subscribe(self, topic: str, delay: int = 0):
        def on_message(client, userdata, msg):  # noqa
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        time.sleep(delay if delay else self.delay)

        self.client_mqtt.subscribe(topic)
        self.client_mqtt.publish(
            topic,
            MqttMessage(
                topic=topic,
                sender="client",
                data={"message": "Master are listening"},
            ).json_str,
        )

        self.client_mqtt.on_message = self.receive_message

    def unsubscribe(self, topic: str):
        try:
            self.client_mqtt.publish(
                topic,
                MqttMessage(
                    topic=topic,
                    sender="client",
                    data={"message": "Master disconnected"},
                ).json_str,
            )
            self.client_mqtt.unsubscribe(topic)
            return True
        except Exception as e:
            print(f"Error in unsubscribe: {e}")
            return False

    def message_handler(self, message):  # noqa
        pass

    def run(self):
        self.client_mqtt.loop_start()

    def stop(self):
        self.client_mqtt.loop_stop()
        self.client_mqtt.disconnect()
        tread = threading.current_thread()
        tread.do_run = False
