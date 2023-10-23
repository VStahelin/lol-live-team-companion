import threading

from cache_manager import get_cache
from constants import MQTT_TOPICS, CACHE_KEYS


class MatchThread(threading.Thread):
    def __init__(self, match_slug):
        threading.Thread.__init__(self)
        self.subscribe_thread = get_cache(CACHE_KEYS.SUBSCRIBER_THREAD)
        self.client_mqtt = None
        self.match_slug = match_slug
        self.mqtt_topics = list(map(lambda topic: f"{match_slug}/{topic}", MQTT_TOPICS))
        self.running = False

    def _subscribe_on_match_topics(self):
        topics = []
        for topic in self.mqtt_topics:
            print(f"Subscribing on topic: {topic}")
            self.subscribe_thread.subscribe(topic)
            topics.append(topic)

        return topics

    def _unsubscribe_from_match_topics(self):
        for topic in self.mqtt_topics:
            print(f"Unsubscribing from topic: {topic}")
            self.subscribe_thread.unsubscribe(topic)

    def run(self):
        try:
            self._subscribe_on_match_topics()
            self.running = True
            return True

        except Exception as e:
            print(f"Error in run match thread: {e}")
            return False

    def stop(self):
        self._unsubscribe_from_match_topics()
        self.running = False
        tread = threading.current_thread()
        tread.do_run = False
