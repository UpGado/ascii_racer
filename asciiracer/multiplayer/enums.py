import enum


class Events(enum.Enum):
    update_score = "update_score"
    id_message = "id_message"  # Used by client to identify itself
