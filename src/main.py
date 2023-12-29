"""Main module. Runs the game"""


from game import Game


def main() -> None:
    """This function runs the game"""
    game = Game()
    game.main_loop()


if __name__ == '__main__':
    main()
