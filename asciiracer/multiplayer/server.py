import json
import logging

from websocket_server import WebsocketServer

from asciiracer.config import SERVER_PORT, SERVER_HOST
from asciiracer.multiplayer.lobby import Lobby
from asciiracer.multiplayer.enums import Events


lobby = Lobby()


def create_id_message(player_id: int):
    data = {
        "event_type": Events.id_message.value,
        "value": int(player_id)
    }
    return json.dumps(data)


def create_score_event_message():
    """
    Create message with event type
    and score table
    :return:
    """
    data = {
        "event_type": Events.update_score.value,
        "value": lobby.score_table
    }

    return json.dumps(data)


def handle_event(event: dict, client: dict, server: WebsocketServer):
    if event["event_type"] == Events.update_score.value:
        lobby.score_table[int(client["id"])] = event["value"]
        server.send_message_to_all(create_score_event_message())


def handle_received_message(client: dict, server: WebsocketServer, message: str):
    handle_event(json.loads(message), client, server)


def handle_new_client_event(client: dict, server: WebsocketServer):
    lobby.create_record_for_new_player(client["id"])
    server.send_message_to_all(create_score_event_message())
    server.send_message(client, create_id_message(client["id"]))


def handle_client_left_event(client: dict, server: WebsocketServer):
    del lobby.score_table[int(client["id"])]


def run_server():
    server = WebsocketServer(
        host=SERVER_HOST,
        port=SERVER_PORT,
        loglevel=logging.INFO
    )
    server.set_fn_new_client(handle_new_client_event)
    server.set_fn_message_received(handle_received_message)
    server.set_fn_client_left(handle_client_left_event)
    server.run_forever()


if __name__ == "__main__":
    run_server()
