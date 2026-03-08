import string
import random

from backend.game.manager import GameManager

rooms = {}


def generate_room_id(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def create_room():
    room_id = generate_room_id()
    rooms[room_id] = GameManager()
    return room_id


def get_room(room_id):
    return rooms.get(room_id)