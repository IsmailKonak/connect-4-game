from Game import Game
game = Game()

print("Welcome to the game")
game.show()
side = None
sit = False
while True:
    print("X's turn.")
    x = int(input("Your move: "))
    sit = game.play(x,"x")
    if sit == True:
        break
    print("Y's turn.")
    y = int(input("Your move: "))
    sit = game.play(y,"y")
    if sit == True:
        break