from game.game import Game
from ai.agent import train

def play_game():
    # Preguntar al usuario sobre el tamaño del tablero
    board_size = 4#int(input("Ingrese el tamaño del tablero (3, 4, 5, 6 u 8): "))
    # train(board_size)
    # user_play = input("¿Quiere jugar como USER o como AI? (U/A): ").lower()
    # if(user_play == "A"):
    #     train(board_size)
    # else:
    game = Game(board_size, user_mode=False)
    for i in range(10):
        game.play_step([1,0,0,0])


if __name__ == "__main__":
    play_game()