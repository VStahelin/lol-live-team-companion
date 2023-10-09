import logging
import threading
import time

from client_watcher.constants import MESSAGE_TYPES, ACTION_TYPES


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
            self.message_handler(message)

        except Exception as e:
            print(f"Error in subscribe callback: {e}")
            print(f"Error in subscribe callback: {msg}")

    def subscribe(self):
        def on_message(client, userdata, msg):  # noqa
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        time.sleep(self.delay)

        self.client_mqtt.subscribe(self.topic)
        self.client_mqtt.on_message = self.receive_message

    def message_handler(self, message):  # noqa
        message_type = message.get("type")
        message_action = message.get("action")
        message = message.get("message")

        if not message_type not in MESSAGE_TYPES and not message:
            raise Exception("Message not valid")

        try:
            match message_type:
                case MESSAGE_TYPES.MESSAGE:
                    print(f"Message: {message}")
                case MESSAGE_TYPES.ACTION:
                    match message_action:
                        case ACTION_TYPES.PING:
                            print(f"Ping: {message}")
                        case ACTION_TYPES.USER_DATA_UPDATE:
                            # This action will be removed when the server is implemented
                            print(f"User data update: {message}")
                        case ACTION_TYPES.USER_DATA_REQUEST:
                            print(f"User data request: {message}")
                case MESSAGE_TYPES.LOG:
                    print(f"Log: {message}")
                    logging.info(message)

                case _:
                    raise Exception("Message not valid")
        except Exception as e:
            print(f"Error in message handler: {e}")
            print(f"Error in message handler: {message}")

    def run(self):
        self.client_mqtt.loop_start()
        thread = threading.current_thread()
        self.subscribe()

        while getattr(thread, "do_run", True):
            time.sleep(0.1)
