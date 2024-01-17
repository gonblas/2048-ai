from game.game import Game
from ai.agent import train

def play_game():
    game = Game()
    game.action = (1,0,0,0)
    game.ai_action_available = True

if __name__ == "__main__":
    play_game()