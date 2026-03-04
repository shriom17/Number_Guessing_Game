from game.logic import check_guess, genrate_random_number
class GameManager:
    def __init__(self):
        self.players=[]
        self.target_number=genrate_random_number()
        self.winner=None

    def add_player(self, player_id):
        if len(self.players) >=2:
            return "Game is full"
        
        if player_id not in self.players:
            self.players.append(player_id)
            return "Player added successfully"
        else:
            return "Player already exists"
        
        if len(self.players) == 2:
            self.start_game()
        
    def start_game(self):
        print("Game started! Guess the number between 1 and 100.")

    def make_guess(self, player_id, guess):
        if player_id not in self.players:
            return "Player not found"
        
        result = check_guess(guess, self.target_number)
        if result == "Sabas Vai, Buke Ay":
            self.winner = player_id
            return f"{result} Player {player_id} wins!"
        else:
            return result
        
    def get_winner(self):
        return self.winner
    
game_manager = GameManager()
game_manager.add_player(1)
game_manager.add_player(2)