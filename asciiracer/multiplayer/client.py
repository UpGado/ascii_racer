import logging
import json
import threading

from websocket import WebSocketApp

from asciiracer.config import SERVER_HOST, SERVER_PORT
from asciiracer.multiplayer.enums import Events


class Client(WebSocketApp):
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        self.score_table = {}
        self.client_running = False
        self.id = None
        self.last_score = 0
        super().__init__(
            url=f"ws://{SERVER_HOST}:{SERVER_PORT}",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )

    def run_client_in_thread(self):
        threading.Thread(
            target=self.run_forever,
            daemon=True
        ).start()
        while not self.client_running:
            ...
        return

    def handle_event(self, event: dict):
        if event["event_type"] == Events.update_score.value:
            self.score_table = event["value"]

        elif event["event_type"] == Events.id_message.value:
            self.id = event["value"]

    def on_open(self, ws: WebSocketApp):
        self.logger.info("open connection with host: {}".format(ws.url))

    def on_message(self, ws, message):
        if not self.client_running:
            self.client_running = True
        self.logger.info("receive message {}".format(message))
        self.handle_event(json.loads(message))

    def on_error(self, ws, error):
        super().close()
        raise ValueError("Error in websocket: {}".format(error))

    def on_close(self, status_code, close_message):
        super().close()
        raise ValueError("Server refuse connection. Close message: {}".format(close_message))

    def send_score_update_message(self, score: int):
        if score == self.last_score:
            return
        self.last_score = score
        message = {"event_type": Events.update_score.value, "value": score}
        self.send_message(message)

    def send_message(self, message: dict):
        self.logger.info("send message {} to host {}".format(message, self.url))
        super().send(json.dumps(message))


if __name__ == "__main__":
    logging.basicConfig()
    client = Client()
    client.logger.setLevel("DEBUG")

    threading.Thread(
        target=client.run_forever,
        daemon=True,
    ).start()

    while not client.client_running:
        ...

    client.send_message({"event_type": Events.update_score.value, "value": 100})
