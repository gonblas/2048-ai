from game.game import Game
from ai.agent import train

def play_game():
    game = Game()
    game._run()


if __name__ == "__main__":
    play_game()