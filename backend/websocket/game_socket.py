from fastapi import APIRouter, WebSocket
from game.manager import GameManager

router = APIRouter()
game_manager = GameManager()

@router.websocket("/ws")
async def game_socket(websocket: WebSocket):
    await websocket.accept()

    player_id = id(websocket)   # simple unique id
    game_manager.add_player(player_id)

    while True:
        data = await websocket.receive_text()
        guess = int(data)

        result = game_manager.make_guess(player_id, guess)

        await websocket.send_text(result)